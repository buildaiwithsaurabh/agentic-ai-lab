from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello FastAPI",
        "author": "Saurabh"
    }


@app.get("/about")
def about():
    return {
        "project": "Agentic AI Lab",
        "backend": "FastAPI"
    }


@app.get("/skills")
def skills():
    return {
        "skills": [
            "Python",
            "FastAPI",
            "AI Engineering",
            "Agentic AI"
        ]
    }