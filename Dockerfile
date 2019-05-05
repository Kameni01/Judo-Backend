FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /judo
WORKDIR /judo
ADD requirements.txt /judo/
RUN pip install -r requirements.txt
ADD . /judo/

