FROM python:alpine3.18
WORKDIR /
COPY . opt
RUN pip install requests
RUN crontab /opt/crontab
RUN chmod +x /opt/entrypoint.sh
CMD ["/opt/entrypoint.sh"]