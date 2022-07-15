FROM python:3

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN pip3 install django==3.0

ENV PYTHONPATH $PYTHONPATH:/code
ENV app_port 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE ${app_port}

WORKDIR /code

# Install Docker from official repo
#RUN apt-get update -qq && \
#    apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
#    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
#    apt-key fingerprint 0EBFCD88 && \
#    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
#    apt-get update -qq && \
#    apt-get install -qqy docker-ce && \
#    usermod -aG docker jenkins && \
#    chown -R jenkins:jenkins $JENKINS_HOME/
#USER jenkins

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]