# Setting up development environment

## Requirements

To be able to run development environment you're required to have installed:
- docker
- docker-compose

## Building development container:

```
git clone git@github.com:corest/nestjs-realworld-example-app.git
cd nestjs-realworld-example-app/dev
docker build -t localhost/nestjsrealworld -f Dockerfile ../
```

## Running development environment

Inside `dev` folder run

```
docker-compose up
```

This will bring up:
- `postgresql` database container
- `web` container with our application.

`web` container entrypoint creates `nestjsrealworld` database, which then used by nodejs application.