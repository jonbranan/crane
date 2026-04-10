#!/bin/sh

CRON_CONFIG_FILE="/etc/crontabs/root"

grep -qF '${CRON} python /opt/crane.py' $CRON_CONFIG_FILE ||echo "${CRON} python /opt/crane.py" >> $CRON_CONFIG_FILE
grep -qF '@reboot' $CRON_CONFIG_FILE || echo "@reboot python /opt/crane.py" >> $CRON_CONFIG_FILE

exec crond -f