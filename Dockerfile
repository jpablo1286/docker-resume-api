FROM python:3
RUN mkdir /opt/resume-api
WORKDIR /opt/resume-api
RUN pip install virtualenv
RUN virtualenv -p python3 .
RUN . bin/activate
RUN bin/pip install --upgrade pip
RUN bin/pip install Django
RUN bin/pip install djangorestframework
RUN bin/pip install mysqlclient
WORKDIR /opt/resume-api/api
CMD while true; do sleep 10; done
