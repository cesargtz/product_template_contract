# -*- coding: utf-8 -*-
{
    'name': "product_template_contract",


    'description': """
        Add new functionality the product
    """,

    'author': "Yecora",
    'website': "yecora.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product',],

    # always loaded
    'data': [
        'security/access_group.xml',
        'security/ir.model.access.csv',
        'views/product_template_contract.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
}
