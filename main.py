from fastapi import FastAPI
from maps import maps_get

app = FastAPI()
app.include_router(maps_get.router)

@app.get("/")
def read_root():
    return {"message": "Taxi 1488"}

#uvicorn main:app --reload