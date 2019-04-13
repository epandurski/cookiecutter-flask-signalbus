FROM python:3.7-alpine
WORKDIR /usr/src/app

ARG FLASK_APP={{cookiecutter.app_slug}}

RUN apk add --no-cache \
    curl \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    git \
    supervisor \
  && pip install --upgrade pip \
  && pip install gunicorn json-logging-py

ENV GUNICORN_LOGLEVEL=warning
ENV GUNICORN_WORKER_CLASS=sync
ENV GUNICORN_WORKERS=2
ENV GUNICORN_THREADS=1
ENV FLASK_APP=$FLASK_APP

# Install "poetry".
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN ln -s "$HOME/.poetry/bin/poetry" "/usr/local/bin"

# Copy the app, install the required packages.
COPY docker/ pyproject.toml poetry.lock wsgi.py ./
COPY src/ src/
RUN poetry config settings.virtualenvs.create false \
  && poetry install --no-dev --no-interaction

# If installed, configure "pudb" debugger not to show a welcome screen.
RUN ! which pudb3 || sed 's/seen_welcome = a/seen_welcome = e034/g' ~/.config/pudb/pudb.cfg -i

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["serve"]
