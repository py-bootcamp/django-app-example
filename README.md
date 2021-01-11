# A simple django app

This repo shows how to containerize a django application based on directly on pip requirements.txt or poetry.

## To build for requirements.txt

```
docker build -t django-app -f Dockerfile.requirements .
```

## To build for poetry

```
docker build -t django-app -f Dockerfile.poetry .
```
