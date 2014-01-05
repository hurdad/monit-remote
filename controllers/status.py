import web
import json
from lib import monit
from models import host

class summary:
    def GET(self):

        #loop hosts
        summary = []
        for myhost in host.get_hosts():
            summary.append(monit.status(myhost));

        #set response header content type to json
        web.header('Content-Type', 'application/json')

        #print json to browser
        return json.dumps(summary)

class status:
    def GET(self, id):

        #get host model
        myhost = host.get_host(id)

        #get status
        mystatus = monit.status(myhost);
     
        #set response header content type to json
        web.header('Content-Type', 'application/json')

        #print json to browser
        return json.dumps(mystatus)

          
