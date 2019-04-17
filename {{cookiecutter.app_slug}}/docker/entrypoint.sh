#!/bin/sh
set -e

logging_conf="$APP_ROOT_DIR/logging.conf"
gunicorn_conf="$APP_ROOT_DIR/gunicorn.conf"

case $1 in
    develop)
        # autoreload on
        shift;
        export FLASK_ENV=development
        exec flask run --host=0.0.0.0 --port $PORT "$@"
        ;;
    debug)
        # autoreload off
        shift;
        export FLASK_ENV=development
        exec python -u wsgi.py "$@"
        ;;
    serve)
        exec gunicorn --config "$gunicorn_conf" --log-config "$logging_conf" -b :$PORT wsgi:app
        ;;
    db)
        shift;
        exec flask db "$@"
        ;;
    signalbus)
        shift;
        exec flask signalbus "$@"
        ;;
    supervisord)
        exec supervisord -c "$APP_ROOT_DIR/supervisord.conf"
        ;;
    *)
        exec "$@"
        ;;
esac
