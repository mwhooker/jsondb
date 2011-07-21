import tornado.ioloop
import tornado.web
from jsondb import JsonDB

store = JsonDB()

class JsonDbHandler(tornado.web.RequestHandler):
    def get(self, path):
        self.write(store.from_path(path))

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
