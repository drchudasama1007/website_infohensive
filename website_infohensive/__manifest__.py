# -*- coding: utf-8 -*-
{
    'name': 'Website Infohensive',
    'summary': "Website Infohensive Page for ERP Platform, App Management, Framework, Contactus, Blog",
    'version': '1.0',
    'category': 'Website',
    'author': 'Bansi',
    'depends': ['base', 'website', 'portal', 'website_crm', 'website_blog'],
    'data': [
        'views/assets.xml',
        'data/data.xml',
        'views/header.xml',
        'views/footer.xml',
	    'views/homepage.xml',
        'views/blog.xml',
        'views/app_management.xml',
        'views/framework.xml',
        'views/contactus.xml',
        'views/erp_plateform.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
