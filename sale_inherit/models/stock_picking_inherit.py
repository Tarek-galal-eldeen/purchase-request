from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.move"

    dimension = fields.Char(string="Product Dimension")


class DraftInvoiceInherit(models.Model):
    _inherit = "account.move.line"

    dimension = fields.Char(string="Product Dimension", readonly=True)
