#!/bin/bash
# Simple startup script for running the Flask app with Gunicorn
# Binds to port 5000 on all interfaces

pip3 install -r requirements.txt
exec gunicorn -b 0.0.0.0:5000 app:app
