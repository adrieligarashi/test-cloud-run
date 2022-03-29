from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "O Marquim é feio"
