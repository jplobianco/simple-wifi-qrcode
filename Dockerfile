ARG VERSION=3.11-slim
FROM python:$VERSION

WORKDIR /app

COPY . .

RUN pip install -e .

WORKDIR /app/src

ENTRYPOINT [ "simple-wifi-qrcode"]
