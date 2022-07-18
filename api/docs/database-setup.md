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

Reference for M1 MacOS: [https://medium.com/signofactory/setting-up-your-mac-as-a-full-stack-web-developer-intel-apple-silicon-in-2021-the-backend-9fcc54e858e3](https://medium.com/signofactory/setting-up-your-mac-as-a-full-stack-web-developer-intel-apple-silicon-in-2021-the-backend-9fcc54e858e3)

## Windows

- Install it all locally (Postgres & pgAdmin)
- Connect using `localhost` and user/pass -> postgres/postgres

## Linux

_See MacOS, and good luck._

## UUID Requirement

Ref: [https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-uuid/](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-uuid/)

Before being able to use UUID in PostgreSQL, run this in your database.

_Install the extension_

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

_Check you can generate UUIDs_

```sql
select uuid_generate_v4();
```