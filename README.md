# Lab 32- Permissions & Postgresql

- Created a Django Rest/Docker app about animals
- This was done on .venv through windows powershell

## Lab Requirements

### Django REST Framework

- Make your site a DRF powered API as you did in previous lab.
- Adjust project’s permissions so that only authenticated user’s have access to API.
- Add a custom permission so that only author of blog post can update or delete it.
- Add ability to switch user’s directly from browsable API.

### Docker

- NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
- create Dockerfile based off python:3.8-slim
- create docker-compose.yml to run Django app as a web service.
- enter docker-compose up --build to start your site.
- add postgres 11 as a service

## Testing

- Manual testing of user access and postgres db working