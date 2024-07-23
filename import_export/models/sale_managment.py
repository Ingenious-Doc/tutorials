from odoo import models, api, fields,_


class sale_order_line(models.Model):
    _inherit="sale.order.line"
    recent_sale_order_line=fields.Many2one(comodel_name='sale.order.line',compute='_last_sale_order',store=True)
    recent_sale_order_date=fields.Date(related=recent_sale_order_line.order_id.date)
    last_price=fields.Float(related=recent_sale_order_line.price_unit)
    

    def _last_sale_order(self):
        last_sale_order=self.env['sale.order.line'].sudo().search([],order='create_date desc',limit=1)
        for record in self:
            if last_sale_order:
                record.recent_sale_order_line=last_sale_order.id
            else:
                record.recent_sale_order_line=False
        


