from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create connection with database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', status_code=status.HTTP_200_OK)
def get_all_blog_posts(db: Session = Depends(get_db)):
    all_blog_posts = db.query(models.Blog).all()
    return all_blog_posts


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_exact_blog(id, response: Response, db: Session = Depends(get_db)):
    blog_post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} is not available!'}

    return blog_post


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_exact_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Info": f"Recond on id {id} has been deleted succesfully!"}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_exact_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return {"Info": f"Recond on id {id} has been updated succesfully!"}

