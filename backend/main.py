import uvicorn
from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from UserManager import UserDataHandler,User
app = FastAPI()



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/users")
def create_user(user: User):
    user_handler =UserDataHandler()
    user_handler.add_user(user)
    return f"Successfully created user {user.name}"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)