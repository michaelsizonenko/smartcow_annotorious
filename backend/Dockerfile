FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY requirements.txt /backend
RUN #apk --update add
RUN #apk add gcc gcc python3-dev libc-dev libffi-dev jpeg-dev zlib-dev libjpeg libxml2-dev libxml2 libxslt-dev

RUN pip install --upgrade pip -r requirements.txt
COPY . /backend
EXPOSE 5000
#
#RUN chmod +x entrypoint.sh
#
#ENTRYPOINT ["entrypoint.sh"]