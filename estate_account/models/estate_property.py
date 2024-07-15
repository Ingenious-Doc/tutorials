from odoo import fields, models,api,Command

class estate_property(models.Model):
    _inherit="estate.property"

    def sold_property_method(self):
        res = super(estate_property,self).sold_property_method()
        journal=self.env['account.journal'].search([("type",'=','sale')],limit=1)

        for prop in self:
            prop.env['account.move'].create({'partner_id':prop.buyer_id.id,'journal_id':journal.id,'move_type':'out_invoice','invoice_line_ids':[Command.create({"name":prop.name,"quantity":1,"price_unit":(prop.selling_price*0.06)}),Command.create({"name":"Admin Fees","quantity":1,"price_unit":100})]})
        return res
