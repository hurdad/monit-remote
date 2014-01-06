import web
import json
from lib import monit
from models import host
import urlparse

class summary:
    def GET(self):


       
        params = urlparse.parse_qs(web.ctx.query)

        callback = None
        if 'callback' in params:
            callback =  params['callback'][0]
   
        #loop hosts
        summary = []
        for myhost in host.get_hosts():
            summary.append(monit.status(myhost));

        #set response header content type to json
        web.header('Content-Type', 'application/json')

        result = {
            'records': [ 
                {
                    'id' : 1,
                    'led' : 1,
                    'hostname' : 'localhost',
                    'cpu' : 100,
                    'mem' : 60,
                    'status' : 1

                }   
            ],
            'totalRecords' : 1
    
        }




        #print json to browser
        if callback is not None:
            return callback + "(" + json.dumps(result) + ")"
        else:
            return json.dumps(result)





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

          
