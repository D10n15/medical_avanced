from odoo import models, fields, api
from datetime import datetime, timedelta

class MedicalNotification(models.Model):
    _name = 'medical.notification'
    _description = 'Medical Notification'

    patient_id = fields.Many2one('medical.patient', string='Patient', required=True)
    appointment_id = fields.Many2one('medical.appointment', string='Appointment', required=True)
    message = fields.Text(string='Message')
    status = fields.Selection([
        ('sent', 'Sent'),
        ('pending', 'Pending'),
        ('failed', 'Failed')
    ], string='Status', default='pending')
    date_sent = fields.Datetime(string='Date Sent')
    sent = fields.Boolean(string='Sent', default=False)

    @api.model
    def send_reminder_notifications(self):
        # Buscar citas programadas en las próximas 24 horas
        upcoming_appointments = self.env['medical.appointment'].search([
            ('date', '>=', fields.Datetime.now()),
            ('date', '<=', fields.Datetime.now() + timedelta(hours=24)),
            ('state', '=', 'scheduled')
        ])

        for appointment in upcoming_appointments:
            # Comprobar si ya existe una notificación pendiente para la cita
            existing_notification = self.search([
                ('appointment_id', '=', appointment.id),
                ('status', '=', 'pending')
            ], limit=1)

            if not existing_notification:
                # Crear una nueva notificación
                self.create({
                    'patient_id': appointment.patient_id.id,
                    'appointment_id': appointment.id,
                    'message': f"Recordatorio: Tiene una cita programada con el Dr. {appointment.doctor_id.name} el {appointment.date}.",
                    'status': 'pending'
                })

    @api.model
    def process_pending_notifications(self):
        # Enviar las notificaciones pendientes
        pending_notifications = self.search([('status', '=', 'pending')])
        for notification in pending_notifications:
            try:
                # Simular envío de mensaje (reemplazar con lógica real de envío)
                # Por ejemplo: self.env['mail.mail'].create({...})
                notification.write({
                    'status': 'sent',
                    'date_sent': fields.Datetime.now(),
                    'sent': True
                })
            except Exception as e:
                notification.write({
                    'status': 'failed'
                })



