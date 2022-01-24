# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '14.0',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment.xml',
        'views/patient_view.xml',
        'views/sale_view.xml',
        'views/patient_gender_view.xml',
        'views/appointments_view.xml',
        'views/doctors.xml',
        'reports/report.xml',
        'reports/purchase_details_template.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
