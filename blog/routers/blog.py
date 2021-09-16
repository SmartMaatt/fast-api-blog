from fastapi import Depends, status, APIRouter
from typing import List
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

# >>> BLOG endpoints
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.BlogOutput)
def create_article(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_article(request, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.BlogOutput])
def get_all_articles(db: Session = Depends(get_db)):
    return blog.get_all_articles(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogOutput)
def get_article_by_id(id, db: Session = Depends(get_db)):
    return blog.get_article_by_id(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_article_by_id(id, db: Session = Depends(get_db)):
    return blog.delete_article_by_id(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_article_by_id(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_article_by_id(id, request, db)
