import os
import web
import json
import tempfile
from lib import pysftp
from models import host

class list:
    def GET(self, id):

        #get host model        
        myhost = host.get_host(id)

        #connect to remote sftp
        ssh = pysftp.Connection(myhost.ssh_ip, myhost.ssh_username, myhost.ssh_private_key)
    
        #list config directorys contents
        mylist = srv.listdir(myhost.monit_config_directory)

        #set response header content type to json
        web.header('Content-Type', 'application/json')
        
        #print json to browser
        return json.dumps(mylist)

class crud:

    def GET(self, id, name):

        #get host model
        myhost = host.get_host(id)

        #connect to remote sftp
        ssh = pysftp.Connection(myhost.ssh_ip, myhost.ssh_username, myhost.ssh_private_key)

        #create temp file        
        fi, path = tempfile.mkstemp()

        #download config to temp file
        ssh.get( myhost.monit_config_directory + name, path)

        #read temp file
        with open(path, 'r') as f:
            data = f.read()

        #remove temp file         
        os.unlink(path)

        #print data to browser
        return data
       
    def POST(self, id, name):
        
        #get data from post
        post_data = web.input()  
       
        #get host model  
        myhost = host.get_host(id)

        #connect to remote sftp
        ssh = pysftp.Connection(myhost.ssh_ip, myhost.ssh_username, myhost.ssh_private_key)

        #generate temp file        
        fi, path = tempfile.mkstemp()

        #write config data to temp file
        with open(path, 'w') as f:
            f.write(post_data.data)

        #upload temp file to remote monit config directory
        ssh.put(path, myhost.monit_config_directory + name)

        #remove temp file         
        os.unlink(path)

        #print result to browser
        return 'ok'

    def DELETE(self, id):
  
        #get host model  
        myhost = host.get_host(id)

        #connect to remote sftp
        ssh = pysftp.Connection(myhost.ssh_ip, myhost.ssh_username, myhost.ssh_private_key)

        #delete remote monit config 
        ssh.execute('rm -f ' + myhost.monit_config_directory + name)

        #print result to browser
        return 'ok'

     

