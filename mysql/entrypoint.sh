#!/bin/bash
set -e

if [ ! -d '/var/lib/mysql/mysql' -a "${1%_safe}"='mysqld' ]; then
	mysql_install_db --user=mysql --datadir=/var/lib/mysql &>/dev/null || true
fi
chown -R mysql:mysql /var/lib/mysql

/usr/bin/supervisord -n 