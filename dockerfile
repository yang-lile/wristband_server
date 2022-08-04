FROM python:3.10.5

MAINTAINER LILUA

ENV PYTHONUNBUFFERED 1

COPY pip.conf /root/.pip/pip.conf

RUN mkdir -p /var/www/html/wrist_band
WORKDIR /var/www/html/wrist_band
ADD . /var/www/html/wrist_band

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone
# RUN sed -i 's/\r//' ./start.sh

# RUN chmod +x ./start.sh
# CMD [ "/bin/sh", "-c", "python3", "./manager.py", "runserver", "0.0.0.0:8000" ]
ENTRYPOINT [ "./start.sh" ]
