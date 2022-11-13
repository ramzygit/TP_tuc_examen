"""
Get items
"""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import actions, schemas
from app.utils.utils import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all items
        Default limit is 100
    """
    items = actions.get_items(database, skip=skip, limit=limit)
    return items
