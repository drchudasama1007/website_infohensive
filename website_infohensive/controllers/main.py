from odoo import fields, http, tools, _
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.website.controllers.main import Website
from odoo.http import request
import json
import base64


class CustomerPortal(http.Controller):

    @http.route(["/blog"], type='http', auth="public", website=True)
    def blog_page(self, page=0, *args, **kwargs):
        return request.render('website_infohensive.blog_template', {})

    @http.route(["/app-management"], type='http', auth="public", website=True)
    def app_management_page(self, page=0, *args, **kwargs):
        return request.render('website_infohensive.app_management_template', {})\

    @http.route(["/framework"], type='http', auth="public", website=True)
    def framework_page(self, page=0, *args, **kwargs):
        return request.render('website_infohensive.framework_template', {})\

    @http.route(["/erp-platform"], type='http', auth="public", website=True)
    def erp_platform_page(self, page=0, *args, **kwargs):
        return request.render('website_infohensive.erp_plateform_template', {})

class HomePageModifications(Website):
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        return request.render('website_infohensive.home_template', {})