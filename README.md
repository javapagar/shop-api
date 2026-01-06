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