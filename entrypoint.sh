#!/bin/sh

CRON_CONFIG_FILE="/opt/crontab"

echo "${CRON} python /opt/crane.py" > $CRON_CONFIG_FILE

exec supercronic -passthrough-logs -quiet $CRON_CONFIG_FILE