from odoo import models, api, fields,_

class product_template(models.Model):
    _inherit='product.template'

    rental_approval_ids=fields.Many2many(comodel_name='approval.request',compute=)