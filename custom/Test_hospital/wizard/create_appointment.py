# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class CreateAppointmentWiz(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    datetime = fields.Datetime(string='Date', required=False)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'datetime': self.datetime
        }
        appointments_rec = self.env['hospital.appointments'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointments',
            'res_id': appointments_rec.id,
            'target': 'new'
        }

    def action_view_appointment(self):
        action = self.env.ref('Test_hospital.action_hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action
