import time

import tornado.ioloop
import tornado.ioloop

import api.device
import base.url_handler as handler
from rabbitmq import example_publisher, example_cosumer

application = handler.Application(
    **{'pika_publisher': example_publisher, 'debug': True,'pika_consumer': example_cosumer})

# 装载 Request Handler 模块
application.load_handler_module(api.device)

if __name__ == "__main__":
    application.listen(8080)
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_timeout(time.time() + .1, example_publisher.run)
    ioloop.add_timeout(time.time() + .1, example_cosumer.run)
    ioloop.start()
