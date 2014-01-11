from lib import monit
from models import host

class start:

    def POST(self, id, name):
        myhost = host.get_host(id)
        return monit.start(myhost, name)
      
class stop:

    def POST(self, id, name):
        myhost = host.get_host(id)
        return monit.stop(myhost, name)

class restart:

     def POST(self, id, name):
        myhost = host.get_host(id)
        return monit.restart(myhost, name)

class monitor:

    def POST(self, id, name):
        myhost = host.get_host(id)
        return monit.monitor(myhost, name)

class unmonitor:

    def POST(self, host, name):
        myhost = host.get_host(id)
        return monit.unmonitor(myhost, name)
