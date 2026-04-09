#!/bin/sh

CRON_CONFIG_FILE="/etc/crontabs/root"

echo "${CRON} python /opt/crane.py" > $CRON_CONFIG_FILE
echo "@reboot python /opt/crane.py" >> $CRON_CONFIG_FILE

exec crond -f