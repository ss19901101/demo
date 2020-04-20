import tornado.ioloop
import tornado.web

import tornado.ioloop
import base.url_handler as handler
import api.device

application = handler.Application()

# 装载 Request Handler 模块
application.load_handler_module(api.device)

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


