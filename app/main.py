from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "application": "DevSecOps Secure CI/CD",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }