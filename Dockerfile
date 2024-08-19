FROM python:3.12.2

WORKDIR /api

RUN apt-get update
RUN apt-get -y install build-essential curl
RUN apt-get -y upgrade


ENV VIRTUAL_ENV=/opt/venv \
        PATH="/opt/venv/bin:$PATH"

ADD https://astral.sh/uv/install.sh /install.sh

RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

COPY ./requirements.txt ./

RUN /root/.cargo/bin/uv venv /opt/venv && \
        /root/.cargo/bin/uv pip install --no-cache -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

COPY ./src ./

EXPOSE 9090

CMD fastapi run --host 0.0.0.0 --port 9090 --workers 4;