FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN mkdir -p /var/www/html/staticfiles

WORKDIR /app
ADD core /app
ADD requirements.txt /app/requirements.txt
ADD entrypoint.sh /app/entrypoint.sh
RUN chmod +x entrypoint.sh
RUN apt-get update \
    && apt-get install -y git
RUN git init
RUN apt-get install -y gcc python3-dev \
    && apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev \
    && apt-get install -y default-mysql-client default-libmysqlclient-dev \
    && apt-get install -y nginx \
    && wget https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm get-pip.py \
    && pip install -r requirements.txt \
    && apt-get -y install systemctl
ADD site-config /etc/nginx/sites-available/site-config
RUN ln -s /etc/nginx/sites-available/site-config /etc/nginx/sites-enabled/ \
    && rm /etc/nginx/sites-enabled/default

EXPOSE 80

CMD "/app/entrypoint.sh"