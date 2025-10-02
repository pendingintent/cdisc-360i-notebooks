#!/bin/sh
pg_initd=/etc/init.d/postgresql

echo "PostgreSQL is ready to create clinical database tables..."
python3 db-import.py
