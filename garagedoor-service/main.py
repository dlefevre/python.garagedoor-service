#!/usr/env/python3

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/toggle")
def toggle_door():
    return {"status": "toggling door"}