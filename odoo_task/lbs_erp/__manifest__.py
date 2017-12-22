# -*- coding: utf-8 -*-
{
    'name': "LBS ERP",

    'summary': """Test module""",

    'description': """
        Test module for LBS Corporation
    """,

    'author': "Nick",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        # 'views/main.xml',
        'views/views.xml',
        # 'views/test.xml',
        # 'views/test_session.xml',
        # 'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': 0,
    'application': True,
}
