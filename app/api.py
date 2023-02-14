from fastapi import FastAPI

app = FastAPI()
from app.model import PostSchema

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]


@app.get('/')
async def read_root() -> dict:
    return  {'message': 'yes'}


@app.get('/posts', tags=['posts'])
async def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    try:
        post = posts[id]
        return {"data": post}
    except IndexError:
        return {"error": "There is no peace in the world until this post isn't existed"}


@app.post('/posts', tags=['posts'])
async def create_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "status": 'post is added'
    }
