from tornado import gen
from tornado.escape import json_decode

from base.http_client import client_api
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
        yield from gen.sleep(10)
        data = {
            'id': body_data['id']
        }
        response = yield client_api.get('resmgr/dev', data)
        print(response.code)
