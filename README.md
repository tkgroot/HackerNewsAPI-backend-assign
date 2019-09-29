# Readme

## Installation

Download and install [Docker for Windows](https://docs.docker.com/docker-for-windows/) or [Docker for Mac](https://docs.docker.com/docker-for-mac/) and [Docker-Compose](https://docs.docker.com/compose/install/) if not present on your system. If
installed run the following to start the api-service.

```bash
docker-compose up -d --build    # -d run in detached mode (optional)
```

### Your Done

The API is reachable under [http://localhost:5000/](http://localhost:5000) and serves the following endpoints:

```bash
/twenty_five_stories  # taks 1
/days_of_posts        # task 2
/karma_stories        # task 3
```

#### Experimental branch

Checkout git branch `f/web`

```bash
docker-compose down   # stopping docker-compose if still running
git checkout f/web
docker-compose up -d --build
```

Browse to [http://localhost:8080](https://localhost:8080)
