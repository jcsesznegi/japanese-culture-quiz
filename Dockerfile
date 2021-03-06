
# start from base
FROM ubuntu:16.04
MAINTAINER Jason Csesznegi <jcsesznegi@gmail.com>

# install system-wide deps for python
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev

# copy our application code
ADD flask-app /opt/flask-app
WORKDIR /opt/flask-app

# fetch app specific deps
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000

# start app
CMD [ "python", "./app.py" ]
