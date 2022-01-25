FROM ubuntu
USER root
RUN mkdir -pv /root/.pip
COPY ./requirements.txt /tmp/requirements.txt
COPY ./pip.conf /root/.pip/pip.conf
COPY ./main_cron /tmp/
RUN sed -i 's/archive.ubuntu.com/mirrors.tencentyun.com/g' /etc/apt/sources.list \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y python python3-pip cron \
    && echo "python3 install success" \
    && pip install -r /tmp/requirements.txt \
    && cp /tmp/main_cron /etc/cron.d/main_cron
RUN chmod 0644 /etc/cron.d/main_cron
RUN crontab /etc/cron.d/main_cron
RUN touch /var/log/cron.log