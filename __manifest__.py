# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : MasterData : All',
    'version': '17.0.0.0.2',
    'summary': (
        'Meta-module — installs all 8 MasterData_* modules in dependency order. '
        'Upgrading it cascades to every declared MasterData_* dep. '
        'One install seeds every domain (Common, Accounting, Stock, Sales, Purchase, '
        'MRP, HR, Repair).'
    ),
    'description': """
Jinasena : MasterData : All
============================

Meta-module. No data of its own — depends on all 8 domain MasterData
repos so a single install seeds every test-env master data set.

Load order (topologically resolved by Odoo via depends):
  Common (currencies, companies, banks, sequences) →
  Accounting (COA, journals, taxes) →
  Stock (products, warehouses, UOMs) →
  Sales + Purchase + MRP (business-domain records) →
  HR + Repair (support-domain records)
""",
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'Jinasena_MasterData_Common',
        'Jinasena_MasterData_Accounting',
        'Jinasena_MasterData_Stock',
        'Jinasena_MasterData_Sales',
        'Jinasena_MasterData_Purchase',
        'Jinasena_MasterData_MRP',
        'Jinasena_MasterData_HR',
        'Jinasena_MasterData_Repair',
    ],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
