# -*- coding: utf-8 -*-
{
    'name': 'Website Infohensive',
    'summary': "Website Infohensive Page for ERP Platform, App Management, Framework, Contactus, Blog",
    'version': '1.0',
    'category': 'Website',
    'author': 'Bansi',
    'depends': ['base', 'website', 'portal'],
    'data': [
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
	    'views/homepage.xml',
        'views/blog.xml',
        'views/app_management.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
