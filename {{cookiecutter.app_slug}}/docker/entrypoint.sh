#!/bin/sh
set -e

# During development, we should be able to connect to services
# installed on "localhost" from the container. To allow this, we find
# the IP address of the docker host, and then in the value of each
# variable which name ends with "_URL" we substitute "localhost" with
# that IP address.
host_ip=$(ip route show | awk '/default/ {print $3}')
for envvar_name in $(env | grep -oE '^[A-Z_]+_URL\b'); do
    eval envvar_value=\$$envvar_name;
    eval export $envvar_name=$(echo "$envvar_value" | sed -E "s/(.*@|.*\/\/)localhost\b/\1$host_ip/")
done

case $1 in
    develop)
        shift;
        flask signalbus flush -w 0
        exec flask run --host=0.0.0.0 --port $PORT --without-threads "$@"
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
