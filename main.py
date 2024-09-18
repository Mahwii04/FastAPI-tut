from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post_form(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    rating: int


class Login(BaseModel):
    username: str
    password: str
    ref_code: str | None = None

@app.get("/")
def index():
    return {'message': 'Hello World'}


@app.get("/posts")
def post():
    return {'data': 'here are some posts for you'}

@app.post("/posts/{id}")
def make_posts(id):
    return {'posts': ' post id is here'}

@app.get("/names")
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


@app.get('/login')
async def login(login: Login):
    return {"message": "Login Here"}