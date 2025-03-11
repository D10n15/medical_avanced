from odoo import http
from odoo.http import request, Response

class MedicalAppointmentAPI(http.Controller):

    @http.route('/api/appointments', type='json', auth='user', methods=['GET'])
    def get_appointments(self, **kwargs):
        """Obtener todas las citas médicas"""
        appointments = request.env['medical.appointment'].search([])
        data = [{
            'id': appt.id,
            'patient': appt.patient_id.name,
            'doctor': appt.doctor_id.name,
            'date': appt.date,
            'state': appt.state
        } for appt in appointments]
        return {'status': 'success', 'data': data}

    @http.route('/api/appointments', type='json', auth='user', methods=['POST'])
    def create_appointment(self, **kwargs):
        """Crear una nueva cita médica"""
        if not all(k in kwargs for k in ('patient_id', 'doctor_id', 'date')):
            return {'status': 'error', 'message': 'Missing required fields'}

        appt = request.env['medical.appointment'].create({
            'patient_id': kwargs['patient_id'],
            'doctor_id': kwargs['doctor_id'],
            'date': kwargs['date'],
            'state': 'scheduled'
        })
        return {'status': 'success', 'appointment_id': appt.id}

    @http.route('/api/appointments/<int:appt_id>', type='json', auth='user', methods=['PUT'])
    def update_appointment(self, appt_id, **kwargs):
        """Actualizar una cita médica"""
        appt = request.env['medical.appointment'].browse(appt_id)
        if not appt.exists():
            return {'status': 'error', 'message': 'Appointment not found'}

        appt.write(kwargs)
        return {'status': 'success', 'message': 'Appointment updated'}

    @http.route('/api/appointments/<int:appt_id>', type='json', auth='user', methods=['DELETE'])
    def delete_appointment(self, appt_id):
        """Eliminar una cita médica"""
        appt = request.env['medical.appointment'].browse(appt_id)
        if not appt.exists():
            return {'status': 'error', 'message': 'Appointment not found'}

        appt.unlink()
        return {'status': 'success', 'message': 'Appointment deleted'}
