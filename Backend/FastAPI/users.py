from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    email: str
    password: str


users_list = [User(id=1, name="John", surname="Doe", url="https://www.google.com", email="john@gmail.com", password="123456"), User(id=2, name="Jane", surname="Doe", url="https://www.google.com",
                                                                                                                                    email="jane@gmail.com", password="123456"), User(id=3, name="Jack", surname="Doe", url="https://www.google.com", email="jack@gmail.com", password="123456")]


@app.get("/usersjson")
async def usersjason():
    return [{"id": user.id, "name": user.name, "surname": user.surname, "url": user.url, "email": user.email, "password": user.password}]


@app.get("/users")
async def users(id: int, name: str):
    return users_list


@app.get("/users/{user_id}")
async def user(id: int):
    return search_user(id)


@app.get("/usersquery/")
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"message": "User not found"}
