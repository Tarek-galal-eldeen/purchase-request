# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalAppointments(models.Model):
    _name = "hospital.appointments"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointments"
    _order = "reference desc"
    _rec_name = "reference"

    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string='Status', tracking=True)
    note = fields.Text(string='Other Info')
    date = fields.Date(string='Date')
    datetime = fields.Datetime(string="Check up time")
    doctor = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    prescription = fields.Text(string="Prescription")
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
                                            string="Prescription Lines")

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Appointment'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or _('New')
        res = super(HospitalAppointments, self).create(vals)
        return res


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"

    name = fields.Char(string="Medicine", required=True)
    qty = fields.Integer(string="Quantity", required=True)
    appointment_id = fields.Many2one('hospital.appointments', string="Appointment")
