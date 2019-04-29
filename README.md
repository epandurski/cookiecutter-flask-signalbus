# Cookiecutter Flask-SignalBus template

Dockerized [Flask-SignalBus](https://flask-signalbus.readthedocs.io/)
project for [Cookiecutter](https://github.com/audreyr/cookiecutter).

## Quick Start

1. Install Cookiecutter globally:

    ```sh
    $ pip install cookiecutter
    ```

2. Generate the boilerplate:

    ```sh
    $ cookiecutter https://github.com/epandurski/cookiecutter-flask-signalbus.git
    ```

3. Find the `README.rst` file in the newly generated directory, and
   follow the instructions there.

    **NOTE:** You will get an error if you try to start the Docker
    containers. This is because few key files are still missing.

4. Create a new `migrations/` directory by running this command:

    ```sh
    $ flask db init
    ```
