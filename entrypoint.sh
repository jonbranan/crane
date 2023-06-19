#!/bin/sh
CRON_CONFIG_FILE="/opt/crontab"

# CRON
get_env CRON
CRON="${CRON:-"5 * * * *"}"

echo "${CRON} python /opt/crane.py" >> "${CRON_CONFIG_FILE}"

exec supercronic -passthrough-logs -quiet "${CRON_CONFIG_FILE}"