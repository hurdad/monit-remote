import web
from lib import monit
from models import host

render = web.template.render('templates')

class index:

    def GET(self):
        summary = []
      
        #loop hosts
        for myhost in host.get_hosts():
            mystatus = monit.status(myhost)

            #loop statuses
            if mystatus is not None:

                #loop processes
                proc_counter = 0
                for proc in mystatus['processes']:
                    if proc['status'] == '0' and proc['monitored'] == '1':
                        proc_counter = proc_counter + 1

                #loop systems
                for system in mystatus['systems']:

                    if system['swap_kilobyte'] != "N/A":
                        swap_megabyte = int(float(system['swap_kilobyte'])/1024)
                    else:
                        swap_megabyte = "N/A"
        
                    summary.append({
                        'id' : myhost['id'],
                        'url' : myhost['monit_httpd_url'],
                        'system' : system['name'],
                        'status' : system['status'],
                        'monitored' : system['monitored'],
                        'load': system['load_one'] + ', ' + system['load_five'] + ', ' + system['load_fifteen'],
                        'cpu' : float(system['cpu_user'])  + float(system['cpu_system']) + float(system['cpu_wait']),
                        'memory' : system['memory'],
                        'memory_megabyte' : int(float(system['memory_kilobyte'])/1024), 
                        'swap' : system['swap'],
                        'swap_megabyte' : swap_megabyte , 
                        'running_processes' :  proc_counter,
                        'total_processes' : len(mystatus['processes']),
                        'running_percent' : float(proc_counter) / float(len(mystatus['processes'])) * 100
                    })
            else:
                summary.append({
                    'id' : myhost['id'],
                    'url' : myhost['monit_httpd_url'],
                    'system' : 'N/A',
                    'status' : 'unable to connect',
                    'load': 'N/A',
                    'cpu' : 'N/A',
                    'memory' : 0,
                    'memory_megabyte' : 'N/A',
                    'swap' : 0,
                    'swap_megabyte' : 'N/A',   
                    'running_processes' :  0,
                    'total_processes' : 0,
                    'running_percent' : 0.0
                })
  
        return render.index(summary)
       
class details:

    def GET(self, host_id):
        myhost = host.get_host(host_id)
        mystatus = monit.status(myhost)
        if mystatus is None:
            mystatus = {
                'platform' : {},
                'systems' : [{'name':'N/A'}],
                'processes' :[],
                'filesystems' : [],
                'hosts' : []
            }

        return render.details(host_id, mystatus)
       
