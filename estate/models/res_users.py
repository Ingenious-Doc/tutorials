from odoo import fields,api,models

class res_users(models.Model):
    _inherit='res.users'
    property_ids=fields.One2many('estate.property','salesman_id')

