{
    'name': 'Medical Appointment Advanced',
    'version': '1.0',
    'category': 'Medical',
    'summary': 'Módulo avanzado para la gestión de citas médicas',
    'website': 'https://www.ejemplo.com',  # Reemplaza con tu URL real
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/medical_security.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/notification_view.xml',  # Comenta si no existe aún
        'data/email_template.xml',      # Comenta si no existe aún

    ],
    'assets': {
        'web.assets_backend': [
            'medical_appointment_advanced/static/src/css/style.css',
            'medical_appointment_advanced/static/src/js/appointment.js',
        ],
    },
    'installable': True,
    'application': True,
}




