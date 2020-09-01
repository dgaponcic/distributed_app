FROM node@sha256:02b7bdbfe6e647adca1c05de50fb46609210a3b0c1b47d9b7c2513b775abe72c

WORKDIR /usr/app
COPY ./package.json ./
RUN npm install 
COPY ./ ./
CMD ["npm","start"]
