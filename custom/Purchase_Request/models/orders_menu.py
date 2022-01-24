# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OrdersMenu(models.Model):
    _name = "purchase.order"
    _description = "Order Menu"

    name = fields.Char(string='Name', required=True)
    requested_by_id = fields.Many2one(comodel_name="res.users", string="Requested by", required=True,
                                      default=lambda self: self.env.user)
    start_date = fields.Date(string="Start Date", default=datetime.today())
    end_date = fields.Date(string="End Date")
    rejection_reason = fields.Text(string="Rejection Reason", readonly=True, default='N/A')
    order_lines = fields.One2many("order.lines", "purchase_order_id", string="Order Lines")
    total_price = fields.Float(string="Total Price", compute='_compute_total')
    state = fields.Selection(
        [('draft', 'Draft'), ('to_be_approved', 'To Be Approved'), ('approve', 'Approve'), ('reject', 'Reject'),
         ('cancel', 'Cancel')], default='draft')

    def action_draft(self):
        self.state = "draft"

    def action_to_be_approved(self):
        self.state = "to_be_approved"

    def action_approve(self):
        self.state = "approve"
        # template_id = self.env.ref('Purchase_Request.order_confirmation_email_template').id
        # Users = self.env['res.users'].
        # for user in Users.has_group('group_purchase_manager'):
        # Users = self.env['res.users'].search([])
        # for user in Users:
        #     if user.has_group('group_purchase_manager'):
        #         self.env['mail.template'].browse(template_id).send_mail(user.id, force_send=True)

    # def action_reject(self):
    #     self.state = "reject"

    def action_cancel(self):
        self.state = "cancel"

    @api.depends('order_lines.total')
    def _compute_total(self):
        for record in self:
            record.total_price = sum(record.order_lines.mapped('total'))

    @api.constrains('order_lines')
    def _check_exist_product_in_line(self):
        for rec in self:
            exist_product_list = []
            for line in rec.order_lines:
                if line.product_id.id in exist_product_list:
                    raise ValidationError(_('Product should be one per line.'))
                exist_product_list.append(line.product_id.id)
