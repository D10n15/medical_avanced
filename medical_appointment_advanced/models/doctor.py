from odoo import models, fields, api

class MedicalDoctor(models.Model):
    _name = 'medical.doctor'
    _description = 'Medical Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone')  # Campo agregado para el teléfono
    email = fields.Char(string='Email')  # Campo agregado para el correo
    user_id = fields.Many2one('res.users', string='Related User', required=True)  # Asociar al usuario de Odoo
    appointment_ids = fields.One2many('medical.appointment', 'doctor_id', string='Appointments')

    @api.model
    def create(self, vals):
        if 'user_id' not in vals:
            vals['user_id'] = self.env.uid  # Asigna el usuario actual automáticamente
        return super(MedicalDoctor, self).create(vals)

