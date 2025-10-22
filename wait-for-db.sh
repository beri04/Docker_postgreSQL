#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

# Wait for Postgres to become available
until pg_isready -h "$host" -p 5432 -U postgres; do
  >&2 echo "Postgres is unavailable - waiting"
  sleep 2
done

>&2 echo "Postgres is up - executing command"
exec $cmd
