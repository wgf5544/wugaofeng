#!/bin/bash

cp /install/entrypoint.sh /.
cp /install/sanity_check.sh /.

yum install -y epel-release
yum install --enablerepo=epel -y mysql-server

#install supervisord
yum -y install python-setuptools && easy_install supervisor

cat > /etc/supervisord.conf <<EOF
[supervisord]
nodaemon=true

[program:mysql]
stderr_logfile=/var/log/tomcat_err.log
stdout_logfile=/var/log/tomcat_out.log
command=/usr/bin/mysqld_safe --datadir=/var/lib/mysql --socket=/var/lib/mysql/mysql.sock --log-error=/var/lib/mysql/mysqld.log --pid-file=/var/run/mysqld/mysqld.pid --basedir=/usr --user=mysql
autorestart=yes
autostart=yes

[program:sanity]
command=/sanity_check.sh
autorestart=true

EOF
