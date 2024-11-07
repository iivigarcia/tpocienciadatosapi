from typing import Optional
import pandas as pd
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/data")
async def read_data():
    new_data = pd.read_csv('content/data.csv', on_bad_lines='skip')
    new_data.to_json("content/data.json")
    with open('content/data.json', 'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)