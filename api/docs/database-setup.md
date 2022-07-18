# Database Setup

## MacOS

- Run postgres via Docker
    - install Docker Desktop (optional)
    - `docker pull postgres`
    - Run: `docker run -d --name postgres14 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres`

- Connect from pgAdmin
    - download it
    - Connection info: (_notice the environment variables `-e` passed to Docker)
        - host: `localhost`
        - user: `postgres`
        - password: `postgres`

## Windows

- Install it all locally (Postgres & pgAdmin)
- Connect using `localhost` and user/pass -> postgres/postgres

## Linux

_See MacOS, and good luck._