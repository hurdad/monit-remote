monit-remote
============

Monit Remote Configuration Python Web App

* Connects to one or more monit's httpd services
* Remote monit.d configuration via ssh (optional)
  
Requirements
------------
* python-webpy
* python-paramiko

Monit Configuration
------------------
Allow for remote connection to monit httpd
```
 set httpd port 2812 and
     use address 0.0.0.0
     allow 0.0.0.0/0.0.0.0
```

SSH Configuration
-----------------
Run these commands as the same user accnt that runs monit-remote web app
```
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub root@remote-host
```

Quick Start
----------
```
git clone https://github.com/hurdad/monit-remote.git
cd monit-remote
python app.py
```

RPM Packaging
-------------
```
cd rpm
make
sudo yum install rpmbuilder/RPMS/..
```
