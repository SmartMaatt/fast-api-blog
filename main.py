from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Matiq', 'love': 'Olix'}}

@app.get('/blog')
def blog(limit=10, published: bool=True, sort: Optional[str]=None):
    if published:
        return {'data': f'{limit} published blogs from the db.'}
    else:
        return {'data': f'{limit} any blogs from the db.'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}

@app.get('/blog/{id}')
def blog_id(id:int):
    return {'data': {'blog id': id}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
async def create_blog(request: Blog):
    return {'data': f'Created blog post called {request.title}'}
