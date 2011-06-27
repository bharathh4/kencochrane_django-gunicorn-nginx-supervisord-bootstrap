from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import exists

def update_server():
    code_dir = '/opt/django/apps/my_app/current/my_app/'
    with settings(user='django'):
        with cd(code_dir):
            # pull down and update, could be replaced with hg fetch if turned on.
            run("hg pull && hg up")
            
            # change ownership to django just to be safe.
            run("chown -R django:django *")
            
            # if you have a database setup
            #run("/opt/django/apps/my_app/current/bin/python2.6 manage.py syncdb")
            
            # if you have south setup to manage your migrations
            #run("/opt/django/apps/my_app/current/bin/python2.6 manage.py migrate")
            
            # remove all pyc files
            run('find -name "*.pyc" -delete')
            
            # restart the app
            run("supervisorctl restart my_app")
            
            # print status to make sure it restarted correctly
            run('supervisorctl status')