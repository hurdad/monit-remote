import web
import json
from lib import monit
from models import host

class summary:
    def GET(self):


        return 'Hello, web!'

class status:
    def GET(self, id):

        myhost = host.get_host(id)
        print myhost.monit_httpd_url
        mystatus = monit.status(myhost);
     
        #set response header content type to json
        web.header('Content-Type', 'application/json')

        #print json to browser
        #return json.dumps(status)

          
