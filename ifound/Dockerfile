FROM node:14.19.2

WORKDIR /ifound

COPY ./package.json /ifound/package.json

COPY ./package-lock.json /ifound/package-lock.json

RUN npm install

# install simple http server for serving static content
RUN npm install --global http-server