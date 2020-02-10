#! /bin/bash
while true; do
	# check if you can login with the password
	sleep 5
	check=`mysqladmin -uroot -p$MYSQL_ROOT_PASSWORD ping | grep alive`
	if [ -n "$check" ]; then
		break
	fi
	mysqladmin -uroot password 'guest'
done

while true;do
	sleep 60
done
