import web
import json
from models import host

class list:

    def GET(self):
        hosts = host.get_hosts()
        web.header('Content-Type', 'application/json')
        return json.dumps( hosts)
       
class crud:

    def GET(self, id):
        return 'Hello, web!'
       
    def POST(self, id):
        return 'Hello, web!'

    def PUT(self, id):
        return 'Hello, web!'

    def DELETE(self, id):
        return 'Hello, web!'

