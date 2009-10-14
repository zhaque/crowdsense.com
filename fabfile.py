### -*- coding: utf-8 -*- ##
""" based on 
inspired by http://morethanseven.net/2009/07/27/fabric-django-git-apache-mod_wsgi-virtualenv-and-p/
"""

from fabric.api import env, run, sudo, require, put, local

env.project_name = 'yotweets.com'

def production():
    env.hosts = ['yotweets.com']
    env.path = '/webapp/yotweets.com'
    env.user = 'root'
    env.virtualhost_path = "/"
    env.requirements = "requirements.txt"
    env.dev_repos = ['git://github.com/CrowdSense/saaskit-muaccounts.git']
    
# tasks
def test():
    "Run the test suite and bail out if it fails"
    local("cd $(project_name); python manage.py test", fail="abort")

def setup():
    """
    Setup a fresh virtualenv as well as a few useful directories, then run
    a full deployment
    """
    require('hosts', provided_by=[production])
    require('path')
    sudo('aptitude install -y python-setuptools')
    sudo('easy_install pip')
    sudo('pip install virtualenv')
    sudo('aptitude install -y apache2')
    sudo('aptitude install -y libapache2-mod-wsgi')
    # we want rid of the defult apache env
    sudo('cd /etc/apache2/sites-available/; a2dissite default;')
    run('mkdir -p %(path)s; cd %(path)s; virtualenv .;' % {'path': env.path})
    run('cd %s; mkdir src -p;' % env.path)
    
    sudo('apt-get -y install --force-yes nmap unzip wget csstidy build-essential sun-java6-jdk ant subversion git-core mercurial bzr gcc curl python-virtualenv python-git python-imaging python-dev python-setuptools python-egenix-mxdatetime libc6-dev python-ncrypt tofrodos postgresql python-psycopg2 nginx apache2 apache2.2-common apache2-mpm-worker apache2-threaded-dev libapache2-mod-wsgi libapache2-mod-rpaf memcached postfix libmemcache-dev')
        
    sudo('aptitude install -y git-core')
    #run('git config --global github.user Arvi3d')
    #run('git config --global github.password vfhnsirf')
    
    sudo('aptitude install -y tar')
    
    
    
    deploy()
    
def deploy():
    """
    Deploy the latest version of the site to the servers, install any
    required third party modules, install the virtual host and 
    then restart the webserver
    """
    require('hosts', provided_by=[production])
    require('path')
    import time
    #env.release = time.strftime('%Y%m%d%H%M%S')
    install_requirements()
    #install_development_tarball()
    #install_site()
    #symlink_current_release()
    #migrate()
    #restart_webserver()
    
# Helpers. These are called by other functions rather than directly
def install_requirements():
    "Install the required packages from the requirements file using pip"
    require('hosts', provided_by=[production])
    require('path')
    require('requirements')
    
    file_name = 'requirements.txt'
    
    put('%s' % env.requirements, '%s/%s' % (env.path, file_name))
    run('cd %s; pip install -E . -r ./%s' % (env.path, file_name), pty=True)
    
def install_development_tarball():
    "Compress development packages, put them to server, extract."
    require('hosts', provided_by=[production])
    require('path')
    
    local('git archive --format=tar master | gzip > saaskit-main.tar.gz')
    put('saaskit-main.tar.gz', '%s/src/' % env.path)
    run('cd %s/src; tar zxf saaskit-main.tar.gz > saaskit-main' % env.path)
    local('rm saaskit-main.tar.gz')
    
    #local('cd ../../; tar cf - "src" | gzip -f9 > "src.tar.gz"')
    #put("../../src.tar.gz", '%s/' % env.path)
    #run('cd %s; tar zxf src.tar.gz;' % env.path)
    #local('rm -f ../../src.tar.gz')

def install_site():
    "Add the virtualhost file to apache"
    require('hosts', provided_by=[production])
    require('path')
    
    sudo('cd %(path)s; cp $(project_name)%(virtualhost_path)s$(project_name) /etc/apache2/sites-available/')
    sudo('cd /etc/apache2/sites-available/; a2ensite $(project_name)') 
        
def symlink_current_release():
    "Symlink our current release"
    require('release', provided_by=[deploy, setup])
    run('cd $(path); rm releases/previous; mv releases/current releases/previous;', fail='ignore')
    run('cd $(path); ln -s $(release) releases/current')
def migrate():
    "Update the database"
    require('project_name')
    run('cd $(path)/releases/current/$(project_name);  ../../../bin/python manage.py syncdb --noinput')
def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/apache2 restart')
    