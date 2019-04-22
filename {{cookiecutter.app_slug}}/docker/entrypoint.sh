#!/bin/sh
set -e

# We should allow the container to work with RabbitMQ servers
# installed on the host. To do this, we find the IP address of the
# host, and then in "$DRAMATIQ_BROKER_URL" we substitute "localhost"
# with that IP address.
if [[ -n "$DRAMATIQ_BROKER_URL" ]]; then
    host_ip=$(ip route show | awk '/default/ {print $3}')
    export DRAMATIQ_BROKER_URL=$(echo "$DRAMATIQ_BROKER_URL" | sed -E "s/(.*@|.*\/\/)localhost\b/\1$host_ip/")
fi

case $1 in
    develop)
        shift;
        flask signalbus flush -w 0
        exec flask run --host=0.0.0.0 --port $PORT "$@"
        ;;
    serve)
        exec gunicorn --config "$APP_ROOT_DIR/gunicorn.conf" -b :$PORT wsgi:app
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
    tasks-gevent)
        shift;
        exec dramatiq-gevent --processes ${DRAMATIQ_PROCESSES-4} --threads ${DRAMATIQ_GREENLETS-8} "$@"
        ;;
    *)
        exec "$@"
        ;;
esac
