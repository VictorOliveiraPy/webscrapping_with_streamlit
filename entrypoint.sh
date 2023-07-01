#!/bin/bash


uvicorn main:app --host 0.0.0.0 --port 9000 --reload &

sleep 5

streamlit run visualized.py

# Inicia o FastAPI usando o Uvicorn
