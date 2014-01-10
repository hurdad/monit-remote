import web
import json
from models import host

class add:
    def POST(self):
        post_input = web.input()
        success = 1 if host.new_host(post_input) > 0 else 0
        web.header('Content-Type', 'application/json')
        return json.dumps({'success' : success, 'message' : 'DB Error' if success == 0 else  '' })

class rest:
    #get    
    def GET(self, id):
        myhost = host.get_host(id)
        web.header('Content-Type', 'application/json')
        return json.dumps(myhost)     
 
    #edit
    def PUT(self, id):
        put_input = web.input()
        success = 1 if host.update_host(id, put_input) is None else 0
        web.header('Content-Type', 'application/json')
        return json.dumps({'success' : success, 'message' : 'DB Error' if success == 0 else  '' })

    #delete
    def DELETE(self, id):
        success = 1 if host.del_host(id) is None else 0
        web.header('Content-Type', 'application/json')
        return json.dumps({'success' : success, 'message' : 'DB Error' if success == 0 else  '' })
