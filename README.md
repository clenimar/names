# names

Simple app for showing names. This repo contains a simple backend, written in Python, which exposes a REST API for retrieving names. All data is stored in a SQLite3 database.

The frontend is a web-app written in Angular 2.

I recommend using Docker to run the services.

### Backend: build & deploy

```bash
$ cd backend
$ docker build . -t names/backend:0.1
$ docker run -it --rm -p 5001:5001 names/backend:0.1
```

### Frontend: build & deploy

```bash
$ cd names-frontend
$ docker build . -t names/frontend:0.1
$ docker run -it --rm -p 4200:4200 names/frontend:0.1
```

The app will be available at http://localhost:4200/names.

### TODO

* implement endpoints GET /users and POST /users
* allow port customization (through environment variables: ports currently fixed at 5001 and 4200)
* decouple database (MySQL?)
