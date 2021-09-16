from fastapi import Depends, status, APIRouter
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import auth

router = APIRouter(
    tags=['Auth']
)

@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.UserOutputWithList)
def login(request: schemas.UserLoginAuth, db: Session = Depends(get_db)):
    return auth.login(request, db)
