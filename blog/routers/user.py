from fastapi import Depends, status, HTTPException, APIRouter
from .. import schemas, models
from ..database import get_db
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)

# >>> USER ENDPOINTS
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOutputWithList)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.UserOutputWithList)
def get_user_by_id(id, db: Session = Depends(get_db)):
    return user.get_user_by_id(id, db)
