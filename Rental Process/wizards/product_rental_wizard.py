from odoo import models, api, fields,_

 class product_rental_wizard(models.TransientModel):
     _name="product.rental.wizard"
     _description="Rental Wizard"

     date_from=fields.datetime()
     date_to=fields.datetime()
     product_id=fields.Many2many(comodel_name='product.template', compute="action_confirm", store=True)

     def action_confirm(self):
         res= super(product_rental_wizard,self).action_confirm()
         category=self.env['approval.category'].search([("approval_type",'=','rental')],limit=1)
         for request in self:
             request.env['approval.request'].create({})