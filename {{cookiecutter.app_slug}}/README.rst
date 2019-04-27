{{cookiecutter.app_name}}
{{'=' * cookiecutter.app_name|length}}

{{cookiecutter.description}}


Setting up a development environment
------------------------------------

1. Install `docker` and `docker-compose`.

2. To create an `.env` file with reasonable defalut values, run this command::

     $ cp env.development .env

3. Install a `RabbitMQ` server on your computer and either create a
   new RabbitMQ user, or allow the existing `guest` user to connect
   from other hosts (by default, only local connections are allowed
   for `guest`). You may need to alter the firewall rules on your
   computer as well, to allow docker containers to connect to the
   docker host.

4. To start the containers, run this command::

     $ docker-compose up --build -d
