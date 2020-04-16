import tornado.ioloop
import tornado.web

from base.url_handler import URLHandler

URLs = URLHandler()


def make_app():
    return tornado.web.Application(URLs.urls)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
