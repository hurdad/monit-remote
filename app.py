import web

urls = (
    
    #html routes
    '/', 'controllers.html.index',
    '/details/(\d+)', 'controllers.html.details',

    #ajax routes
    '/action/start/(\d+)/(.*)', 'controllers.actions.start',
    '/action/stop/(\d+)/(.*)', 'controllers.actions.stop',
    '/action/restart/(\d+)/(.*)', 'controllers.actions.restart',
    '/action/monitor/(\d+)/(.*)', 'controllers.actions.monitor',
    '/action/unmonitor/(\d+)/(.*)', 'controllers.actions.unmonitor',
    '/host/add', 'controllers.hosts.add',   
    '/host/(\d+)', 'controllers.hosts.rest',
    '/config/(\d+)/(.*?)', 'controllers.configs.rest'
)

web.config.debug = True

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
