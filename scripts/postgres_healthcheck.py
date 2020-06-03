#!/usr/bin/env python3

import psycopg2
import os
import logging
import time

logger = logging.getLogger("postgres-ping")

state = 1
while state > 0:
    try:
        connection = psycopg2.connect(
            dbname=os.environ.get('DATABASE_NAME'),
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD'),
            host=os.environ.get('POSTGRES_IP'),
            port=5432)
        state = connection.closed
        logger.info("Database is ready!")
    except Exception as connection_exception:
        logger.error(connection_exception)
        time.sleep(1)
        pass
