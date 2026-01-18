## Shop API

This API project implements functionality to manage a shopping cart.
It has three main modules:
- users
- products
- shopping cart

Data persistence is implemented using files, following a hexagonal architecture.
For security it uses OAUTH2
The API is built using the FastAPI framework.

### Executing test
`make test`

### Executing project
`make api-dev`

This command starts the server.
You can access the Swagger documentation at:
http://127.0.0.1:8000/docs


## NGINX
It uses a simple proxy reverse with Nginx

## Docker image
You can build a docker image using dockerfile:
`docker build -t <tag_name> .`

You can run a container using:
`docker run -d -p <host-port:docker-port> --name <container-name> <image-tag_name>`

## Docker compose
It helps to deploy two conatiners, one with the API app and other with reverse proxy.
`docker compose up`
If you use docker compose, you must to access throught the reverse proxy with:
http://127.0.0.1/docs

