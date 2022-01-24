# -*- coding: utf-8 -*-
{
    'name': 'Purchase Request',
    'version': '14.0',
    'summary': 'Purchase Request Software',
    'sequence': 5,
    'description': """Purchase Request Software""",
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['sale', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'wizard/reject_wizard.xml',
        'views/order_lines.xml',
        'views/orders_menu.xml',
        'reports/purchase_details_template.xml',
        'reports/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
