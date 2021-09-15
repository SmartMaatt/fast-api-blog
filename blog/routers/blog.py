from fastapi import Depends, status, HTTPException, APIRouter
from typing import List
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

# >>> BLOG endpoints
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.BlogOut)
async def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, owner_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.BlogOut])
def get_all_blog_posts(db: Session = Depends(get_db)):
    all_blog_posts = db.query(models.Blog).all()
    return all_blog_posts


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogOut)
def get_exact_blog(id, db: Session = Depends(get_db)):
    blog_post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} is not available!'}

    return blog_post


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_exact_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Info": f"Recond on id {id} has been deleted succesfully!"}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_exact_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return {"Info": f"Recond on id {id} has been updated succesfully!"}
