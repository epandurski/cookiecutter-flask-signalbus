FROM python:3.7-alpine
WORKDIR /usr/src/app

ARG FLASK_APP={{cookiecutter.app_slug}}

ENV FLASK_APP=$FLASK_APP
ENV POETRY_VERSION="0.12.12"
ENV USE_PIP_VERSION="19.0.3"
ENV USE_GUNICORN_VERSION="19.9.0"

ENV GUNICORN_LOGLEVEL=warning
ENV GUNICORN_WORKER_CLASS=sync
ENV GUNICORN_WORKERS=2
ENV GUNICORN_THREADS=1

RUN apk add --no-cache \
    curl \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    git \
    supervisor \
  && pip install --upgrade pip==$USE_PIP_VERSION \
  && pip install gunicorn==$USE_GUNICORN_VERSION json-logging-py==0.2 \
  && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
  && ln -s "$HOME/.poetry/bin/poetry" "/usr/local/bin"

# Install dependencies.
COPY pyproject.toml poetry.lock ./
RUN poetry config settings.virtualenvs.create false \
  && poetry install --no-dev --no-interaction

# If installed, configure "pudb" debugger not to show a welcome screen.
RUN ! which pudb3 || sed 's/seen_welcome = a/seen_welcome = e034/g' ~/.config/pudb/pudb.cfg -i

# Copy app files.
COPY docker/ wsgi.py ./
COPY $FLASK_APP/ $FLASK_APP/
RUN python -m compileall .
COPY migrations/ migrations/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["serve"]
