FROM python:3.8
MAINTAINER MZS LIMITED

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY ./requirements.txt /requirements.txt
COPY ./start-server.sh /start-server.sh
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser --disabled-password user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/start-server.sh"]
