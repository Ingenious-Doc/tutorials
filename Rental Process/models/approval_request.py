from odoo import models, api, fields,_

class approval_request(models.Model):
    _inherit="approval.request"

    def action_approve(self):
        res=super(approval_request,self).action_approve()