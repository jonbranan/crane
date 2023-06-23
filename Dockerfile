FROM python:alpine3.18
WORKDIR /
COPY . opt
RUN apk add --no-cache supercronic
RUN pip install requests
RUN chmod +x /opt/entrypoint.sh
CMD ["/opt/entrypoint.sh"]