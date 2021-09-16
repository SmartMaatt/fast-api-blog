from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import pwd_cxt

def login(request: schemas.UserLoginAuth, db: Session):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")

    if not pwd_cxt.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid password")

    # TO DO - auth token
    return user
