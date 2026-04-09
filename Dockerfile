FROM python:alpine3.23
WORKDIR /
COPY *.py entrypoint.sh /opt/
RUN pip install requests
RUN chmod +x /opt/entrypoint.sh
CMD ["/opt/entrypoint.sh"]