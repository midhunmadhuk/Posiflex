# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Service Management",
    'summary': "Service management features",
    'description': """
    Includes Features for service management
    """,
    'category': 'Sales',
    'version': '1.1',
    'depends': ['base', 'product'],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/service_ticket_view.xml',
    ],
    'demo': [
    ],
}
