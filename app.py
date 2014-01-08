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
    '/host/list', 'controllers.hosts.list',
    '/host/(\d+)', 'controllers.hosts.crud',
    '/config/list/(\d+)', 'controllers.configs.list',
    '/config/(\d+)/(.*?)', 'controllers.configs.crud'
)

web.config.debug = True

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
