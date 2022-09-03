from fastapi import FastAPI
from flask import Flask
app_fastapi = FastAPI()
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return """Welcome to the rancharound website...

    Under development, 
    
    thanks for visiting, 
    
    come back later."""

@app_fastapi.get("/api")
async def api_root():
    return """Welcome to rancharound' api...

    Under development, 
    
    thanks for visiting, 
    
    come back later."""