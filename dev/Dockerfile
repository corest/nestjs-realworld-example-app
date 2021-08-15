FROM node:14-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev npm python3
RUN pip3 install psycopg2
COPY src /app/src/
COPY dev /app/dev
COPY ormconfig.json.example /app/ormconfig.json
RUN sed -i "s/localhost/db/g" /app/ormconfig.json
COPY src/config.ts.example /app/src/config.ts
COPY package.json index.js jest.json nestconfig.json nodemon.json tsconfig.json /app/

WORKDIR /app
RUN npm install
ENTRYPOINT ["/app/dev/entrypoint.sh"]
