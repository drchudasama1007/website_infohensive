from odoo import fields, http, tools, _
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
import json
import base64


class CustomerPortal(http.Controller):

    @http.route(["/blog"], type='http', auth="public", website=True)
    def blog_page(self, page=0, *args, **kwargs):
        return request.render('website_infohensive.blog_template', {})

