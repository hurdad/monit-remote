import web, datetime
db = web.database(dbn='sqlite', db='db/monit-remote.db')


def get_hosts():
  
    return list(db.select('hosts', order='id DESC'))
    #return db.select('hosts', order='id DESC')

def get_host(id):
    try:
        return db.select('hosts', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_host(title, text):
    db.insert('hosts', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    db.delete('hosts', where="id=$id", vars=locals())

def update_host(id, title, text):
    db.update('hosts', where="id=$id", vars=locals(), title=title, content=text)
