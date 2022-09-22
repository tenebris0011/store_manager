FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app
ADD core /app
ADD requirements.txt /app/requirements.txt
RUN apt-get update \
    && apt-get install -y git
RUN git init
RUN apt-get install -y gcc python3-dev \
    && apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev \
    && apt-get install -y default-mysql-client default-libmysqlclient-dev
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN rm get-pip.py
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]