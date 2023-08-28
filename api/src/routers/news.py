from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    BackgroundTasks
)
from deps.pagination import get_pagination
from models.models import News
from database import get_db
from sqlalchemy.orm import Session

from utils.utils import paginate, response



background_tasks = BackgroundTasks()

router = APIRouter(tags=["Wallet"], prefix="")


