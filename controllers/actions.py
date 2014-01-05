from lib import monit
from models import host

class start:

    def GET(self, id, name):
        myhost = host.get_host(id)
        return monit.start(myhost, name)
      
class stop:

    def GET(self, id, name):
        myhost = host.get_host(id)
        return monit.stop(myhost, name)

class restart:

     def GET(self, id, name):
        myhost = host.get_host(id)
        return monit.restart(myhost, name)

class monitor:

    def GET(self, id, name):
        myhost = host.get_host(id)
        return monit.monitor(myhost, name)

class unmonitor:

    def GET(self, host, name):
        myhost = host.get_host(id)
        return monit.unmonitor(myhost, name)
