# -*- coding: utf-8 -*-
from odoo import api, fields, models


class OrderLines(models.Model):
    _name = "order.lines"
    _description = "Order Menu"

    product_id = fields.Many2one(comodel_name="product.product", string="product_id", required=True)
    description = fields.Char()
    quantity = fields.Float(string="Quantity", default=1)
    cost_price = fields.Float(string="Cost Price")
    total = fields.Float(string="Total")

    purchase_order_id = fields.Many2one('purchase.order', string="Order")

    @api.onchange('product_id', 'quantity')
    def onchange_product_desc(self):
        if self.product_id:
            if self.product_id.name:
                self.description = self.product_id.name
            if self.product_id.standard_price:
                self.cost_price = self.product_id.standard_price
                self.total = self.product_id.standard_price * self.quantity
        else:
            self.description = ""
