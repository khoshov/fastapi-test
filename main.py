from databases import Database
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

database = Database("postgresql://postgres:postgres@db/example")

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    await database.connect()
    now = await database.execute(query="SELECT NOW();")
    return {"new": now}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
