# API template with FastAPI

This is an API template based on FastAPI. The main purpose of this repo is to have a bootstrap FastAPI template in order to build API applications.

## Prerequisites

This template application can be run directly via `uvicorn` or as docker image.

If it needs to be run via [uvicorn], the requirements in the `requirements.txt` should be installed to the environment first by using [pip].

```sh
pip install -r requirements.txt
```

### Running via uvicorn

```sh
uvicorn app.main:app --reload
```

### Running as docker container

> Note that this has been tested with `docker` version `20.10.14` and `docker-compose` version `v2.4`.

In order to build and run the application as docker container, `docker-compose.yml` file can be run with `docker-compose` command.

```sh
docker-compose up --build -d app
```

## Future work / TODO

- Add PostgreSQL docker image to connect.
- Exception handling
- Test cases for all
- GitHub actions for code quality and



[pip]: (https://pip.pypa.io/en/stable/installation/)
[uvicorn]: (https://www.uvicorn.org)