from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/blog')
async def create_blog(request: schemas.Blog):
    return {'data': f'Created blog post: "{request.title}"'}
