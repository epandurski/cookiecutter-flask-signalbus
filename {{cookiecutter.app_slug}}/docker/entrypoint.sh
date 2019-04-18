#!/bin/sh
set -e

logging_conf="$APP_ROOT_DIR/logging.conf"
gunicorn_conf="$APP_ROOT_DIR/gunicorn.conf"

# We should allow the container to work with RabbitMQ server installed
# on the host. To do this, we find the IP address of the host, and
# then in "$DRAMATIQ_BROKER_URL" we substitute each occurrence of the
# special hostname "host.docker.internal" with that IP address.
if [[ -n "$DRAMATIQ_BROKER_URL" ]]; then
    host_ip=$(ip route show | awk '/default/ {print $3}')
    export DRAMATIQ_BROKER_URL=${DRAMATIQ_BROKER_URL//host.docker.internal/$host_ip};
fi


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
    tasks)
        shift;
        exec dramatiq --processes ${DRAMATIQ_PROCESSES-4} --threads ${DRAMATIQ_THREADS-8} "$@"
        ;;
    *)
        exec "$@"
        ;;
esac
