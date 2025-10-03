#!/bin/sh
# Script to setup the database enviromment
docker-compose up -d --force-recreate --build
sleep 10
docker exec -it clinical-database python3 db-import.py
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt