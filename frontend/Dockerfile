FROM node:14-alpine AS alpine
ENV VERSION=v14 NPM_VERSION=latest YARN_VERSION=latest
MAINTAINER MZS LIMITED

COPY ./package.json /package.json
COPY ./package-lock.json /package-lock.json
RUN npm install

RUN mkdir /frontend
WORKDIR /frontend
COPY . /frontend