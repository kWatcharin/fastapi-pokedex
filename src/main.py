from fastapi import FastAPI


app = FastAPI(title="FastAPI-Pokedex")


@app.get("/")
async def main():
    return {
        "detail": "hello, world"
    }