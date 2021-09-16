from fastapi import Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import auth

router = APIRouter(
    tags=['Auth']
)

@router.post('/login', status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.login(request, db)
