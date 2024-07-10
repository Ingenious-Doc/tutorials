from odoo import models,fields
from datetime import datetime

class estate_property_tags(models.Model):
    _name="estate.property.tags"
    _description="Estate Tags"
    name=fields.Char(required=True)
    _order='name'
    property_id=fields.Many2one('estate.property','property_tags')
    _sql_constraints=[
            ('check_unique_name','UNIQUE(name)',
             'The name of the tag must be unique')]
    color=fields.Integer() 
