from odoo import models, api, fields,_

class approval_category(models.Model):
    _inherit="approval.category"
    approval_type=fields.selection(selection_add=[("rental","Rental")])