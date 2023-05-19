import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/api/users")
def create_user(user: User):
    print(user)
    # Process the user data, e.g., save it to a database
    # You can add your own logic here
    # For demonstration purposes, we'll just return the user data
    return f"Successfully created user {user.name}"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)