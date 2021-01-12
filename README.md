# A simple django app

This repo shows how to containerize a django application based on pip requirements.txt, poetry or conda.

## To build for requirements.txt

```
docker build -t django-app -f Dockerfile.requirements .
```

## To build for poetry

```
docker build -t django-app -f Dockerfile.poetry .
```

## To build for conda

```
docker build -t django-app -f Dockerfile.conda .
```

## To build for conda with multistage

```
docker build -t django-app -f Dockerfile.conda-multistage .
```

## To run the image

```
docker run -it -p 8080:8080 django-app
```
