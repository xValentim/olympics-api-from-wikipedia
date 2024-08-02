from fastapi import FastAPI
from dotenv import load_dotenv
from utils import *
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {"STATUS": "OK"}

@app.get("/medal_table")
def medal_table():
    return {"medal_table": get_medal_table()}