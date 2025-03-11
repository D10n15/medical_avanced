from odoo import models, fields, api

class MedicalPatient(models.Model):
    _name = 'medical.patient'
    _description = 'Medical Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)

class MedicalDoctor(models.Model):
    _name = 'medical.doctor'
    _description = 'Medical Doctor'

    name = fields.Char(string='Name', required=True)

class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Medical Appointment'

    patient_id = fields.Many2one('medical.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('medical.doctor', string='Doctor', required=True)
    date = fields.Datetime(string='Appointment Date', required=True)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], string='Status', default='scheduled')

    @api.model
    def creat(self, vals):
        appointment = super(MedicalAppointment, self).create(vals)

        # Validar si el doctor tiene un usuario relacionado y luego un partner_id
        if not appointment.doctor_id.user_id:
            raise ValueError(f"El doctor '{appointment.doctor_id.name}' no tiene un usuario asignado.")

        recipient = appointment.doctor_id.user_id.partner_id
        if not recipient:
            raise ValueError(f"El usuario del doctor '{appointment.doctor_id.name}' no tiene un partner asignado.")

        # Crear la notificación
        self.env['medical.notification'].create({
            'message': f"New appointment scheduled for {appointment.patient_id.name} with Dr. {appointment.doctor_id.name}.",
            'recipient_id': recipient.id,
            'sent': False
        })

        return appointment



        








