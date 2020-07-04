FROM python:3.8-alpine
RUN adduser \
    --disabled-password \
    --home /home/appuser \
    --shell /bin/bash \
    --system \
    --uid 1000 \
    appuser
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --upgrade setuptools wheel
RUN apk update && apk add --no-cache \
    build-base \
    curl \
    gcc \
    libc-dev \
    linux-headers \
    musl-dev \
    nginx \
    openssl \
    openssl-dev \
    pcre-dev \
    rsyslog \
    supervisor
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN pip install uwsgi
RUN chown -R appuser /var/lib/nginx/ /var/log/nginx /run/ /home/appuser/
# RUN chmod -R 0777 /var/lib/nginx/ /var/log/nginx /run/
RUN rm /etc/nginx/conf.d/default.conf
WORKDIR /home/appuser
USER appuser
COPY . .
COPY ./uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY ./supervisord.conf /etc/supervisord.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
EXPOSE 5000
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
