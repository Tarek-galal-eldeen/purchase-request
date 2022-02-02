# -*- coding: utf-8 -*-
{
    'name': 'Sales inherit ',
    'version': '14.0',
    'sequence': 1,
    'category': 'Accounting/Accounting',
    'depends': ['sale_stock'],
    'data': [
        'views/dimensions_view.xml',
        'views/stock_picking_dimension.xml',
        'views/invoice_dimension.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
