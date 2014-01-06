import web
from lib import monit
from models import host

render = web.template.render('templates')

class index:

    def GET(self):
        return render.index('test')
       
class host:

    def GET(self, id):
      #  myhost = host.get_host(id)
      #  mystatus = monit.status(myhost);
        return render.host('tst')
       
