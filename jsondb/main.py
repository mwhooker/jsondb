import httplib
import logging
import json
import tornado.ioloop
import tornado.web
from jsondb import JsonDB

store = JsonDB({'test': {'foo': 'bar'}})
log = logging.getLogger(__name__)

class JsonDbHandler(tornado.web.RequestHandler):

    def abort(self, err=500):
        raise tornado.web.HTTPError(err)

    def get_error_html(self, status_code, **kwargs):
        resp = {
            'code': status_code,
            "message": httplib.responses[status_code]
        }
        return resp

    def data_from_request(self):
        mime = self.request.headers.get('Content-Type')
        type, subtype = mime.split('/')

        data = None
        if mime == 'application/json':
            try:
                data = json.loads(self.request.body)
            except ValueError, e:
                pass
        elif type == 'text':
            data = self.request.body

        return data


    def get(self, path, **kwargs):
        try:
            data = store[path]
        except KeyError, e:
            self.abort(404)
        self.write(data)

    def post(self, path, *args, **kwargs):
        if path in store:
            log.debug("data exists at this path")
            self.abort(403)

        data = self.data_from_request()
        if not data:
            self.abort(400)
        store[path] = data

        resp = {
            'link': path,
            'data': data
        }

        self.set_status(201)
        self.write(resp)

    def put(self, path):
        pass

    def delete(self, path):
        try:
            del store[path]
        except KeyError, e:
            self.abort(404)

if __name__ == "__main__":
    application = tornado.web.Application([
            (r"/(.*)", JsonDbHandler),
        ], debug=True
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
