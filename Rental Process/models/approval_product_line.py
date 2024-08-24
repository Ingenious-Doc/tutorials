from odoo import models, api, fields,_

class approval_product_line(models.Model):
    _inherit="approval.product.line"
    rental_date_from=fields.datetime()
    rental_date_to=fields.datetime()