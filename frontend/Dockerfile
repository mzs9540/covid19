FROM node:14-alpine AS alpine
ENV VERSION=v14 NPM_VERSION=latest YARN_VERSION=latest
MAINTAINER MZS LIMITED

COPY ./package.json /package.json
COPY ./package-lock.json /package-lock.json
RUN npm install latest-version

RUN mkdir /frontend
WORKDIR /frontend
COPY . /frontend

RUN adduser --disabled-password user
RUN chown -R user:user /frontend/
RUN chmod -R 755 /frontend/node_modules
USER user