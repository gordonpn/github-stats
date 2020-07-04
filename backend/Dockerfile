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
RUN apk add --no-cache \
    gcc \
    libc-dev \
    musl-dev \
    openssl-dev
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN chown appuser /home/appuser
WORKDIR /home/appuser
USER appuser
COPY . .
EXPOSE 5000
CMD ["python", "./main.py"]
