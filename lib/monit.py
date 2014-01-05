import urllib
import urllib2
import libxml2

types = {0: 'Filesystem', 1: 'Directory', 2: 'File', 3: 'Daemon', 4: 'Connection', 5: 'System'}

def status(host):

    url = host.monit_httpd_url + '/_status?format=xml'
    xml = get_request(url, host.monit_httpd_username, host.monit_httpd_password)
    xdoc = libxml2.parseDoc(xml)
    


def start(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'start' }
    return post_request(url, host.monit_httpd_username, host.monit_httpd_poassword, data)

def stop(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'stop' }
    return httpd.post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)

def restart(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'restart' }
    return post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)

def monitor(host, name): 
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'monitor' }
    return post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)

def unmonitor(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'unmonitor' }
    return post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)



def post_request(url, username, password, data):

    if username is not None:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)

    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)

    try:
        f = urllib2.urlopen(req)     
    except IOError, e:
        print e

    return r.read()
      

def get_request(url, username, password):

    print username
    print password
    
    if username is not None:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)

    try:
        f = urllib2.urlopen(url)     
    except IOError, e:
        print e

    return f.read()



class system:
    def __init__(self):
        self.name
        self.status
        self.monitored
        self.load
        self.cpu
        self.memory
        self.swap
        self.uptime

class filesystem:
    def __init__(self):
        self.name
        self.status
        self.monitored
        self.percent
        self.usage
        self.total

class process:
    def __init__(self):
        self.name
        self.status
        self.monitored
        self.pid
        self.uptime
        self.memory
        self.cpu

class host:
    def __init__(self):
        self.name
        self.status
        self.monitored
        self.response_time
