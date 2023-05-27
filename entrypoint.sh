#!/bin/bash

gunicorn server:app --bind 0.0.0.0:8089