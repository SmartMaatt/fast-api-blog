from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session

def create_article(request: schemas.Blog, db: Session):
    new_article = models.Blog(title=request.title, body=request.body, owner_id=1)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all_articles(db: Session):
    all_articles = db.query(models.Blog).all()
    return all_articles


def get_article_by_id(id, db: Session):
    article = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} is not available!'}

    return article


def delete_article_by_id(id, db: Session):
    article = db.query(models.Blog).filter(models.Blog.id == id)
    if not article.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
    article.delete(synchronize_session=False)
    db.commit()
    return {"Info": f"Recond on id {id} has been deleted succesfully!"}


def update_article_by_id(id, request: schemas.Blog, db: Session):
    article = db.query(models.Blog).filter(models.Blog.id == id)
    if not article.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available!')
    article.update({'title': request.title, 'body': request.body})
    db.commit()
    return {"Info": f"Recond on id {id} has been updated succesfully!"}
