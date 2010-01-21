### -*- coding: utf-8 -*- ##

import os
from fabric.api import env

from saaskit.fabfile import ifnotsetted
from saaskit.fabfile import install_packages, install_mail_transfer_agent, log_setup
from saaskit.fabfile import github_config, postgresql_setup, postgresql_user_db_flush
from saaskit.fabfile import webapp_setup, install_project, update_project, build_source
from saaskit.fabfile import nginx_config, apache2_config, restart_webserver

env.SOURCE_PATH = 'src/answers'
env.git_path = 'git@github.com:CrowdSense/answers.git'

def production():
    #env.hosts = []
    
    ifnotsetted('host_string', 'crowdsense.com', True, 
        "No hosts found. Please specify (single) host string for connection")
    ifnotsetted('user', 'root', True, "Server user name")
    ifnotsetted('VPS_IP', '97.107.138.174', True, "VPS IP")
    ifnotsetted('POSTGRES_USER', 'crowdsense', True, "PostgreSQL user name")
    ifnotsetted('POSTGRES_PASSWORD', 'crowdsenseS3n89mkk', True, "PostgreSQL user's password")
    ifnotsetted('POSTGRES_DB', 'crowdsense', True, "PostgreSQL DATABASE")
    ifnotsetted('UBUNTU_VERSION', 'jaunty', True, "Ubuntu version name")
    ifnotsetted('PAYPAL_EMAIL', 'admin_1255085897_biz@crowdsense.com', True, "PAYPAL EMAIL")
    ifnotsetted('PAYPAL_TEST', 'True', True, "PAYPAL TEST (True or False)?", r'^(True|False)$')
    