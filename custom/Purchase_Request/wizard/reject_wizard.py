from odoo import api, fields, models, _


class RejectWizard(models.TransientModel):
    _name = "create.reject.wizard"
    _description = "Create Reject Wizard"

    rejection_reason = fields.Text(string="Rejection Reason", required=True)

    def action_reject_order(self):
        self.env['purchase.order'].browse(
            self.env.context.get('active_id', False)).rejection_reason = self.rejection_reason
        self.env['purchase.order'].browse(self.env.context.get('active_id', False)).state = 'reject'
