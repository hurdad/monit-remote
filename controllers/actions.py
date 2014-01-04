class start:

    def GET(self, host_id, name):
        return 'Hello, web!' + host_id + name
      

class stop:

    def GET(self, host_id, name):
        return 'Hello, web!' + host_id + name

class restart:

     def GET(self, host_id, name):
        return 'Hello, web!' + host_id + name
      
class monitor:

    def GET(self, host_id, name):
        return 'Hello, web!' + host_id + name

class unmonitor:

    def GET(self, host_id, name):
        return 'Hello, web!' + host_id + name
