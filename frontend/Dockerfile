FROM node:14
ENV VERSION=v14 NPM_VERSION=latest YARN_VERSION=latest
MAINTAINER MZS LIMITED

RUN mkdir /frontend
WORKDIR /frontend
COPY . /frontend
RUN npm install latest-version

RUN ls