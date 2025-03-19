#!/bin/bash 
pip install --no-cache-dir -r requirements.txt 

uvicorn main:app --host 0.0.0.0 --port 8080
