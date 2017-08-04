# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales Modification',
    'version': '10.0.1.0.0',
    'category': 'Sales',
    'summary': 'Modification of sales module',
    'author': 'Muhammad Syarif',
    'website': 'http://www.mhdsyarif.com',
    'license': 'AGPL-3',
    'depends': ['sale', 'crm', 'web'],
    'data': [
        'views/template.xml',
        'views/channel_crm_view.xml',
    ],
    'images': ['static/description/odoo.png'],
    'installable': True,
    'auto_install': False
}
