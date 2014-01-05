import web
import json
from models import host

class list:

    def GET(self):
        hosts = host.get_hosts()
        web.header('Content-Type', 'application/json')
        return json.dumps(hosts)
       
class crud:

    def GET(self, id):
        myhost = host.get_host(id)
        web.header('Content-Type', 'application/json')
        return json.dumps(hosts)     
       
    def POST(self, id):
        post_input = web.input()
        return host.new_host(post_input)

    def PUT(self, id):
        return  host.update_host(id, data)

    def DELETE(self, id):
        return  host.del_host(id)

