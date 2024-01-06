from databases import Database
from fastapi import FastAPI

database = Database("postgresql://postgres:postgres@db/example")

app = FastAPI(debug=True)


@app.get("/")
async def root():
    await database.connect()
    now = await database.execute(query="SELECT NOW();")
    return {"new": now}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
