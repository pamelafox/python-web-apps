# Python Web Apps: Teaching Materials

This repository contains the teaching materials for a 5-part Python Web Apps workshop series,
as well as additional links and resources that may be useful for students and teachers.

* [Workshop Series](#workshop-series)
* [Example Projects](#example-projects)
* [Talks](#talks)

## Workshops

Each workshop has a set of slides with exercises interleaved.
We recommend giving students at least 20 minutes for each exercise and to allow ample time for exercise review and questions,
so each workshop takes about 2.5-3 hours to teach.

The workshop series is designed to be taught in the following order:

| Title   | Slides | Slide files | Topics |
| ------- | ------ | ----------- | ------ |
| Flask, Routing, Templates | [View online](https://pamelafox.github.io/python-web-apps/flask-web-apps-workshop/) | [See in repo](/flask-web-apps-workshop/) | Introduction to HTTP, web apps, setting up a Flask app, routing, and templates |
| Databases and ORMs | [View online](https://pamelafox.github.io/python-web-apps/db-web-apps-workshop/) | [See in repo](/db-web-apps-workshop/) |  Introduction to databases, SQLAlchemy, and Django |
| HTTP APIs| [View online](https://pamelafox.github.io/python-web-apps/http-apis-workshop/) | [See in repo](/http-apis-workshop/) | Introduction to HTTP APIs and FastAPI |
| Containerization | [View online](https://pamelafox.github.io/python-web-apps/containers-workshop/) | [See in repo](/containers-workshop/) | Introduction to Docker and containerization for Python web apps |
| Testing Web Apps | [View online](https://pamelafox.github.io/python-web-apps/testing-web-apps-workshop/) | [See in repo](/testing-web-apps-workshop/)  | Testing Python web apps with pytest and Playwright |

The slides are built using [Reveal.js](https://revealjs.com/) and are written in HTML.
The exercises are GitHub repositories with [dev containers](https://code.visualstudio.com/docs/devcontainers/containers)
for easy usage in GitHub Codespaces and VS Code.

## Example projects

These repositories can be used as starting points for student projects (and some of them are already used in the exercises).
All repositories contain instructions for running the app locally, and many of them contain instructions for deploying to Azure.
Other cloud providers can be used as well, but the steps would be different.

### Flask/Quart

| Repository    | Description  |
| ------------- |:-------------|
| [simple-flask-server-example](https://github.com/pamelafox/simple-flask-server-example) | A very simple Flask server |
| [simple-flask-server-container](https://github.com/pamelafox/simple-flask-server-container) | A very simple Flask server, containerized with Docker |
| [simple-flask-api-container](https://github.com/pamelafox/simple-flask-api-container) | An HTTP API built with Flask, containerized with Docker |
| [flask-charts-api-container-app](https://github.com/pamelafox/flask-charts-api-container-app) | A charts API built with APIFlask and containerized with Docker |
| [flask-gallery-container-app](https://github.com/pamelafox/flask-gallery-container-app) | A gallery app built with Flask and containerized with Docker |
| [flask-db-quiz-example](https://github.com/pamelafox/flask-db-quiz-example) | A quiz app built with Flask, PostgreSQL and SQLAlchemy |
| [flask-surveys-container-app](https://github.com/pamelafox/flask-surveys-container-app) | A surveys app built with Flask, PostgreSQL and SQLAlchemy, containerized with Docker |
| [azure-flask-postgres-flexible-appservice](https://github.com/Azure-Samples/azure-flask-postgres-flexible-appservice) | A tourism website built with Flask and PostgreSQL |
| [azure-flask-postgres-flexible-aca](https://github.com/Azure-Samples/azure-flask-postgres-flexible-aca) | A tourism website built with Flask and PostgreSQL, containerized with Docker |
| [msdocs-flask-postgresql-sample-app-azd](https://github.com/pamelafox/msdocs-flask-postgresql-sample-app-azd)     | A restaurant review app built with Flask and PostgreSQL |

### Django

| Repository    | Description  |
| ------------- |:-------------|
| [django-quiz-app](https://github.com/pamelafox/django-quiz-app) | A quiz app built with Django and PostgreSQL |
| [azure-django-postgres-flexible-aca](https://github.com/Azure-Samples/azure-django-postgres-flexible-aca) | A tourism website built with Django and PostgreSQL |
| [azure-django-postgres-flexible-appservice](https://github.com/Azure-Samples/azure-django-postgres-flexible-appservice) | A tourism website built with Django and PostgreSQL, containerized with Docker |
| [msdocs-django-postgresql-sample-app-azd](https://github.com/pamelafox/msdocs-django-postgresql-sample-app-azd)     | A restaurant review app built with Django and PostgreSQL |

### FastAPI

| Repository    | Description  |
| ------------- |:-------------|
| [simple-fastapi-container](https://github.com/pamelafox/simple-fastapi-container) | A very simple FastAPI server, containerized with Docker |
| [staticmaps-function](https://github.com/pamelafox/staticmaps-function) | A static maps API built with FastAPI |
| [regression-model-azure-demo](https://github.com/pamelafox/regression-model-azure-demo)     | A regression model API built with FastAPI |
| [azure-fastapi-postgres-flexible-appservice](https://github.com/Azure-Samples/azure-fastapi-postgres-flexible-appservice) | A tourism website built with FastAPI and PostgreSQL |
| [azure-fastapi-postgres-flexible-aca](https://github.com/Azure-Samples/azure-fastapi-postgres-flexible-aca) | A tourism website built with FastAPI and PostgreSQL, containerized with Docker |

## Talks

These recordings cover topics related to the workshop materials, so they may be helpful for teachers or students using these materials.

| Talk    | Video  | Slides | Description  |
| ------------- |:-------------| :-----| :-----|
| Containerization 101 with Docker and Flask | [Video](https://www.youtube.com/watch?v=87iqvFFaX6U) | [Slides](https://pamelafox.github.io/my-py-talks/flaskcontainers/) | Interactive workshop that introducses Docker and containerization for Flask web apps |
| Writing Python Web Apps with VS Code | [Video](https://www.youtube.com/watch?v=AO9yHm8zKsk) | [Slides](https://pamelafox.github.io/my-py-talks/python-apps-vscode/) | Customizing VS Code to work on Python web apps (Django specifically) - Dev Containers, Debugging, Testing, etc.
| 1-click deploys of Python web apps to Azure | [Video](https://www.youtube.com/watch?v=XeDwYnuuTWI) | [Slides](https://pamelafox.github.io/my-py-talks/iac-deploys/) | Deploying Python web apps to Azure using the Azure Developer CLI |
| Using PostgreSQL in VS Code | [Video](https://www.youtube.com/watch?v=JTHTWp9DIZQ&t=93s) | -- | Using PostgreSQL in VS Code Dev Containers and Codespaces, using Docker and SQLTools extension |

## Feedback

If you have any feedback on the materials, or if you'd like to contribute, please [open an issue](/issues) or [submit a pull request](/pulls). You can also open an issue if you're looking for materials or examples on a specific topic.