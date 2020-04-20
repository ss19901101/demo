import tornado.ioloop
import tornado.ioloop

import base.url_handler as handler
from mock import mock_api

application = handler.Application()

# 装载 Request Handler 模块
application.load_handler_module(mock_api)

if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()




