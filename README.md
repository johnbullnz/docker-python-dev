# docker-python-dev

*Docker application*

This is a template for a Python app running inside a Docker container. It consists of a `docker-compose.yml` file so that it can be run using Docker Compose and extended with other services (e.g. a database).

The `app` service is set to run `main.py` as a cronjob every minute. This can be modified as required. stdout and stderr are sent to the docker container logging system, so can be accessed using `docker-compose logs`.

A custom `.bashrc` file is included to set up a colourised bash prompt.

## Development with vscode

1. Start by running `docker-compose up -d`

1. Using the Docker extension go to *Remote Explorer >> Containers*, right click on the container and select *Attach to Container*.


## Production

The following lines can be removed from the `app` section of `docker-compose.yml`:

```
    volumes:
      - ./app:/app  # can be removed in production
```
