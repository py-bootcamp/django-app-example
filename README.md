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

## To run the image

```
docker run -it -p 8080:8080 django-app
```

## Deployment

Create a Kubernetes cluster with [k3d](https://k3d.io/)

```
k3d cluster create my-cluster -p "8081:80@loadbalancer" --agents 2
```

## Deploy app, service and ingress

```
kubectl apply -f infrastructure/
```
