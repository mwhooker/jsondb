import tornado.ioloop
import tornado.web
from jsondb import JsonDB

store = JsonDB({'test': {'foo': 'bar'}})

class JsonDbHandler(tornado.web.RequestHandler):
    def get(self, path, **kwargs):
        try:
            data = store[path]
        except KeyError, e:
            self.send_error(404)
        self.set_header('Content-type', 'application/json')
        self.write(data)

    def post(self, path):
        pass

    def put(self, path):
        pass

    def delete(self, path):
        pass

if __name__ == "__main__":
    application = tornado.web.Application([
            (r"/(.*)", JsonDbHandler),
        ], debug=True
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
