#!/usr/bin/env sh

gunicorn main:"test_app()" -b 0.0.0.0:5000 --reload