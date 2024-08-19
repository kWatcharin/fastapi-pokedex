FROM python:3.12.2

WORKDIR /api

RUN apt-get update
RUN apt-get upgrade

COPY ./requirements.txt ./

RUN pip install --no-cache-dir uv

RUN uv pip install --no-cache-dir -r requirements.txt

COPY ./src/* ./

EXPOSE 9090

CMD fastapi run --host 0.0.0.0 --port 9090 --workers 4;