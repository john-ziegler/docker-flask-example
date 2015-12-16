FROM centos7
MAINTAINER John Ziegler <zieglerj@mskcc.org>
RUN yum install -y python-pip
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
ADD . /opt/webapp
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python", "app.py"]