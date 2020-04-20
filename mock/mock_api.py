from tornado import gen

from base.url_handler import route
import base.url_handler as handler

CACHE = {}


@route("/mock")
class MockAPI(handler.RequestHandler):

    @gen.coroutine
    def get(self):
        id = self.request.get_argument(name='id')

    @gen.coroutine
    def post(self):
        body_data = self.request.body
        print(body_data)
