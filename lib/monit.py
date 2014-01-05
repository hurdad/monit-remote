import urllib
import urllib2
import libxml2

types = {0: 'Filesystem', 1: 'Directory', 2: 'File', 3: 'Daemon', 4: 'Connection', 5: 'System'}

def status(host):

    url = host.monit_httpd_url + '/_status?format=xml'
    (code, xml) = get_request(url, host.monit_httpd_username, host.monit_httpd_password)  
    if code != 200:
        return None
    
    doc = libxml2.parseDoc(xml)
     
    #system
    systems = []
    ctxt = doc.xpathNewContext()
    for system in ctxt.xpathEval("//service[@type=5]"):
        ctxt.setContextNode(system)

        system_tuple = {
            'name' : ctxt.xpathEval('name')[0].getContent(),
            'status' : ctxt.xpathEval('status')[0].getContent(),
            'monitor' : ctxt.xpathEval('monitor')[0].getContent(),
            'load_one' : ctxt.xpathEval('system/load/avg01')[0].getContent(),
            'load_five' : ctxt.xpathEval('system/load/avg05')[0].getContent(),
            'load_fifteen' : ctxt.xpathEval('system/load/avg15')[0].getContent(),
            'cpu_user' : ctxt.xpathEval('system/cpu/user')[0].getContent(),
            'cpu_system' : ctxt.xpathEval('system/cpu/system')[0].getContent(),
            'cpu_wait' : ctxt.xpathEval('system/cpu/wait')[0].getContent(),
            'memory' : ctxt.xpathEval('system/memory/percent')[0].getContent(),
            #swap = ctxt.xpathEval('system/swap/percent')[0].getContent(),
            'uptime' : ctxt.xpathEval('//server/uptime')[0].getContent()
        }
        systems.append(system_tuple);

    #filesystem  
    filesystems = []
    ctxt = doc.xpathNewContext()  
    for fs in ctxt.xpathEval("//service[@type=0]"):
        ctxt.setContextNode(fs)

        fs_tuple = {
            'name' : ctxt.xpathEval('name')[0].getContent(),
            'status' : ctxt.xpathEval('status')[0].getContent(),
            'monitored' : ctxt.xpathEval('monitor')[0].getContent(),
            'percent' : ctxt.xpathEval('block/percent')[0].getContent(),
            'usage' : ctxt.xpathEval('block/usage')[0].getContent(),
            'total' : ctxt.xpathEval('block/total')[0].getContent()
        }
        filesystems.append(fs_tuple);

    #processes
    processes = []
    ctxt = doc.xpathNewContext()  
    for proc in ctxt.xpathEval("//service[@type=3]"):
        ctxt.setContextNode(proc)

        proc_tuple = {
            'name' : ctxt.xpathEval('name')[0].getContent(),
            'status' : ctxt.xpathEval('status')[0].getContent(),
            'monitored' : ctxt.xpathEval('monitor')[0].getContent(),
            'pid' : ctxt.xpathEval('pid')[0].getContent(),
            'uptime' : ctxt.xpathEval('uptime')[0].getContent(),
            'memory' : ctxt.xpathEval('memory')[0].getContent(),
            'cpu' : ctxt.xpathEval('cpu')[0].getContent()
        }
        processes.append(proc_tuple);

    #hosts
    hosts = []
    ctxt = doc.xpathNewContext()  
    for host in ctxt.xpathEval("//service[@type=4]"):
        ctxt.setContextNode(host)

        host_tuple = {
            'name' : ctxt.xpathEval('name')[0].getContent(),
            'status' : ctxt.xpathEval('status')[0].getContent(),
            'monitored' : ctxt.xpathEval('monitor')[0].getContent(),
            'response_time' : ctxt.xpathEval('port/resoponsetime')[0].getContent()
        }
        hosts.append(host_tuple);
 
    #build data structure
    data = {'system' : systems, 'filesystem' : filesystems, 'processes' : processes, 'hosts' : hosts}
    
    #clean up
    doc.freeDoc()
    ctxt.xpathFreeContext()

    return data

def start(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'start' }
    (code, body) = post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)
    return code

def stop(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'stop' }
    (code, body) = post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)
    return code
    
def restart(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'restart' }
    res = post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)
    return res['code']   
    
def monitor(host, name): 
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'monitor' }
    (code, body) = post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)
    return code

def unmonitor(host, name):
    url = host.monit_httpd_url + "/" + name
    data = {'action' : 'unmonitor' }
    (code, body) = post_request(url, host.monit_httpd_username, host.monit_httpd_password, data)
    return code
   
def post_request(url, username, password, data):

    #http auth
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

    return ( f.getcode(), f.read() )
      

def get_request(url, username, password):
    
    #http auth
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

    return ( f.getcode(), f.read() )
    
