# from odoo import http


# class GitTest(http.Controller):
#     @http.route('/git_test/git_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/git_test/git_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('git_test.listing', {
#             'root': '/git_test/git_test',
#             'objects': http.request.env['git_test.git_test'].search([]),
#         })

#     @http.route('/git_test/git_test/objects/<model("git_test.git_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('git_test.object', {
#             'object': obj
#         })

