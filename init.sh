#!/bin/bash
echo "SELECT 'CREATE DATABASE megafon_db' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'megafon_db')\gexec" | psql
