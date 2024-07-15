from odoo import fields, models,api

class estate_property(models.Model):
    _inherit="estate.property"

    def sold_property_method(self):
        res = super(estate_property,self).sold_property_method()
        return res
