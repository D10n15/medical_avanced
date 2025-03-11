from odoo import models, fields, api

class MedicalPatient(models.Model):
    _name = 'medical.patient'
    _description = 'Medical Patient'

    name = fields.Char(string='Patient Name', required=True)
    birth_date = fields.Date(string='Birth Date')  # Campo agregado
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    phone = fields.Char(string='Phone')  # Campo agregado
    email = fields.Char(string='Email')  # Campo agregado
    appointment_ids = fields.One2many('medical.appointment', 'patient_id', string='Appointments')

