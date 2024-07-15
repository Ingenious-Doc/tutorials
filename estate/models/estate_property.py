from odoo import models, fields,api,_
from odoo.tools.float_utils import float_compare,float_is_zero
from odoo.exceptions import UserError,ValidationError
from datetime import datetime
class estate_property(models.Model):
    _name="estate.property"
    _description="Estate properties"
    active=fields.Boolean('Active',default=True,tracking=True)
    name=fields.Char(required=True)
    _order="id desc"
    
    state=fields.Selection(
           default='new' ,string='State',
                selection=[('new',"New"),('received',"Offer Received"),('accepted','Offer Accpted'),('sold','Sold'),('cancel','Canceled')])
    description=fields.Text()
    postcode=fields.Char()
    #
    property_type=fields.Many2one("estate.property.type",string="Property Type")
    property_tags=fields.Many2many("estate.property.tags", string='Property Tags')
    salesman_id=fields.Many2one("res.users",string="Salesman")
    offers=fields.One2many("estate.property.offer","property_id",string="Offers")
    best_price=fields.Float(defualt=1,compute="_best_offer",stored=True)
    status=fields.Selection(string='Status',readonly=True,selection=[('new',"New"),('sold', 'Sold'),('cancelled','Cancelled')])
    #
    selling_price=fields.Integer(readonly=True)
    date_availability=fields.Date(default=datetime.today())
    expected_price=fields.Float(required=True)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
    string='Type',
        selection=[('south', 'South'),('north','North'),('east','East'),('west',"West")])
    total_area=fields.Float(compute="_total_area")

    _sql_constraints=[
            ('check_selling_price','CHECK(selling_price>=0)',
             'Selling price must be greater than 0'),
            ('check_expected_price','CHECK(expected_price>0)',
             'Expected price must be greater than 0'),
            ('unique_constraint','UNIQUE(name)',
             'Name of property must be unique')]
    def _total_area(self):
        for record in self:
            record.total_area=record.garden_area+record.living_area
            return True

    
    def _best_offer(self):
        for record in self:
            if len(record.offers.mapped('price'))!=0:
                record.best_price=max(record.offers.mapped("price"))
                return True
            else:
                record.selling_price=0
                record.best_price=0
    

    
    @api.ondelete(at_uninstall=False)
    def _unlink_if_new(self):
        if self.state!='new' and self.state!='cancel':
            raise UserError("can't delete a not cancelled or new record")




    @api.constrains('selling_price')
    def _check_best_price(self):
        for record in self:
            if float_compare(0.9,1-(record.best_price/record.expected_price),precision_rounding=1)<=0 and not float_is_zero(record.selling_price,precision_rounding=0.01):
                raise ValidationError("Selling price must be greater than or equal to 90% of expected price")
    def reset_state(self):
        for record in self:
            record.state='new'
            record.status='new'
    def sold_property_method(self):
        for record in self:
            if record.state=="accepted":
                record.status='sold'
                record.state='sold'
            elif record.state=='new':
                raise UserError("Please accept and offer first")
            else:
                raise UserError('Cancelled Property cannot be sold')
    def cancelled_property_method(self):
        for record in self:
            if record.status!="sold":
                record.status='cancelled'
                record.state='cancel'
            else:
                raise UserError('Sold Property cannot be cancelled')
