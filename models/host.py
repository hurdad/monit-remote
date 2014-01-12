import os, sys, web, datetime

db = web.database(dbn='sqlite', db='db/monit-remote.db')

def get_hosts():
    return list(db.select('hosts', order='id ASC'))

def get_host(id):
    try:
        return db.select('hosts', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_host(data):
    try:
        id = db.insert('hosts', monit_httpd_url=data['monit_httpd_url'],  monit_httpd_username=data['monit_httpd_username'], monit_httpd_password=data['monit_httpd_password'], monit_config_directory=data['monit_config_directory'], monit_binary_path=data['monit_binary_path'], ssh_ip=data['ssh_ip'], ssh_username=data['ssh_username'],  ssh_private_key=data['ssh_private_key'])
    except : 
        id = 0
    return id

def del_host(id):
    try:
        db.delete('hosts', where="id=$id", vars=locals())
        retval = 1
    except : 
        retval = 0
        return retval

def update_host(id, data):
    print data
    try:
        db.update('hosts', where="id=$id", vars=locals(), monit_httpd_url=data['monit_httpd_url'],  monit_httpd_username=data['monit_httpd_username'], monit_httpd_password=data['monit_httpd_password'], monit_config_directory=data['monit_config_directory'], monit_binary_path=data['monit_binary_path'], ssh_ip=data['ssh_ip'], ssh_username=data['ssh_username'],  ssh_private_key=data['ssh_private_key'])
        retval = 1
    except : 
        retval = 0
        return retval
