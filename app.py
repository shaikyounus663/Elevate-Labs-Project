echo 'from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, CI/CD with GitHub Actions and Docker!"}
' > app.py

