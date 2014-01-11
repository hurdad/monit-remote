import os
import web
import json
import re
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

    def GET(self, host_id, name):
        
        #validate name
        p = re.compile('^\.')
        if p.match(name) is not None:
            return json.dumps({'success' : 0, 'message' : 'invalid name'})    

        #get host model
        myhost = host.get_host(host_id)

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
        return json.dumps(data)     
       
    def POST(self, host_id, name):

        #validate name
        p = re.compile('^\.')
        if p.match(name) is not None:
            return json.dumps({'success' : 0, 'message' : 'invalid name'})    

        #get data from post
        post_data = web.input()  
        print post_data
       
        #get host model  
        myhost = host.get_host(host_id)

        #connect to remote sftp
        ssh = pysftp.Connection(myhost.ssh_ip, myhost.ssh_username, myhost.ssh_private_key)

        #generate temp file        
        fi, path = tempfile.mkstemp()

        #write config data to temp file
        with open(path, 'w') as f:
            f.write(post_data['data'])

        #upload temp file to remote monit config directory
        ssh.put(path, myhost.monit_config_directory + name)

        #remove temp file         
        os.unlink(path)
    
        #check for config error
        error = True
        res = ssh.execute(myhost.monit_binary_path + " -t")
        for row in res:
            print row
            if row == 'Control file syntax OK\n':
                error = False
                break

        #clean up if error
        if error:
            #remote newly added config
            ssh.execute("rm -f " + myhost.monit_config_directory + name)
            return json.dumps({'success' : 0, 'message' : res})
            
        #monit reload
        ssh.execute(myhost.monit_binary_path + " reload")
        
        #print result to browser
        return json.dumps({'success' : 1, 'message' : ''})
     
    def DELETE(self, host_id, name):

        #validate name
        p = re.compile('^\.')
        if p.match(name) is not None:
            return json.dumps({'success' : 0, 'message' : 'invalid name'})    

        #get host model  
        myhost = host.get_host(host_id)

        #connect to remote sftp
        ssh = pysftp.Connection(myhost.ssh_ip, myhost.ssh_username, myhost.ssh_private_key)

        #delete remote monit config 
        ssh.execute('rm -f ' + myhost.monit_config_directory + name)

        #monit reload
        ssh.execute(myhost.monit_binary_path + " reload")

        #print result to browser
        return json.dumps({'success' : 1, 'message' : ''})


