#!/bin/sh

# create db
python3 /app/dev/setup_db.py
# start server
node /app/index.js