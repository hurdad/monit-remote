import web
from classes.hello import hello

urls = (
  '/', 'hello')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
