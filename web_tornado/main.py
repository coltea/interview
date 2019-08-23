import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import HTTPClient


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, tornado")


router_lt = [
    (r"/", MainHandler),
]


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


class App(object):
    def __init__(self, ip, port, router_lt):
        self.ip = ip
        self.port = port
        self.router_lt = router_lt

    def run(self):
        app = tornado.web.Application(self.router_lt)
        app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    app = App('0', 8888, router_lt)
    app.run()
