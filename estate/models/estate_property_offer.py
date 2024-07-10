from odoo import models, fields,api,_
from datetime import datetime,timedelta
from odoo.exceptions import UserError,ValidationError
class estate_property_offer(models.Model):
    _name="estate.property.offer"
    _description="Estate offers"
    _order="price desc"
    name=fields.Char()
    price=fields.Float()
    offer_status=fields.Selection(string="Status",readonly=True, selection=[('accepted',"Accepted"),('refused',"Refused")])
    partner_id=fields.Many2one('res.partner', required=True)
    property_id=fields.Many2one('estate.property',required=True)
    validity= fields.Integer(default=7)
    date_deadline=fields.Date(compute="_compute_deadline",default=datetime.now(),inverse="_compute_validity")
    property_type_id=fields.Many2one(related='property_id.property_type')

    _sql_constraints=[
            ('check_price', 'CHECK(price>0 )','The offer price must be greater than 0'),
                     ]
    def _compute_deadline(self):
        for record in self:
            record.date_deadline=datetime.now()+timedelta(days=record.validity)
    

    def _compute_validity(self):
        for record in self:
            record.validity=(record.date_deadline-datetime.now().date()).days
    
    #Borrowed code... testing couldn't really understand this
    @api.model
    def create(self,vals):
        if vals.get("property_id") and vals.get("price"):
            prop = self.env["estate.property"].browse(vals["property_id"])
            # We check if the offer is higher than the existing offers
            if prop.offers:
                max_offer = max(prop.mapped("offers.price"))
                if float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise UserError("The offer must be higher than %.2f" % max_offer)
            prop.state = "received"
        return super().create(vals)
    
    def accept_offer(self):
        for record in self:
            if 'accepted' in record.property_id.offers.mapped('offer_status'):
                raise UserError('You already accpeted another offer! Please refuse it to accept this one')
            else:
                record.property_id.selling_price=record.price 
                record.offer_status='accepted'
                record.property_id.state='accepted'

    def refuse_offer(self):
        for record in self:
            record.offer_status='refused'

