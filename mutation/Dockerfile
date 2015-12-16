FROM centos:7
MAINTAINER John Ziegler <zieglerj@mskcc.org>
ADD ./requirements.txt /tmp/requirements.txt
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install -qr /tmp/requirements.txt
ADD . /opt/webapp
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python", "app.py"]
