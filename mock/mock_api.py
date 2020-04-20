from tornado import gen
from tornado.escape import json_decode

from base.url_handler import route
import base.url_handler as handler

CACHE = {}


@route("/mock")
class MockAPI(handler.RequestHandler):

    @gen.coroutine
    def get(self):
        request_id = int(self.get_argument(name='id'))
        print(CACHE)
        if request_id in CACHE:
            self.finish('ACTIVE')
        else:
            self.finish('unknown')

    @gen.coroutine
    def post(self):
        body_data = json_decode(self.request.body)
        self.finish('OK')
        yield from gen.sleep(2)
        CACHE[body_data['id']] = body_data
