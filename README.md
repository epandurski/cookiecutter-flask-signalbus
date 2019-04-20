# Cookiecutter Flask-SignalBus template

Dockerized Flask-SignalBus project for [Cookiecutter](https://github.com/audreyr/cookiecutter).

## Quick Start

Install Cookiecutter globally:

```sh
$ pip install cookiecutter
```

Generate the boilerplate:

```sh
$ cookiecutter https://github.com/epandurski/cookiecutter-flask-signalbus.git
```

Then:

```sh
$ poetry lock
$ flask db init
```
