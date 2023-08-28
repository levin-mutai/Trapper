from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    BackgroundTasks
)
from api.src.deps.pagination import get_pagination
from api.src.models.models import News
from database import get_db
from sqlalchemy.orm import Session

from api.src.utils.utils import paginate, response



background_tasks = BackgroundTasks()

router = APIRouter(tags=["Wallet"], prefix="")

router.get("/")
def get_news(
    
    background_tasks: BackgroundTasks,
    pagination:dict = Depends(get_pagination),
    db: Session = Depends(
        get_db,
    ),
    ):
    """
    Get news.
    """
    news = db.query(News).all()
    
    return paginate(res=news,pagination=pagination)  

router.get("/categories")
def get_category(
    background_tasks: BackgroundTasks,
    pagination:dict = Depends(get_pagination),
    db: Session = Depends(
        get_db,
    ),
    ):
    
    """
    Get news.
    """

    return response(res="res")    
router.get("/categories/{category}")
def get_news_by_category(
    category:str,

    background_tasks: BackgroundTasks,
    pagination:dict = Depends(get_pagination),
    db: Session = Depends(
        get_db,
    ),
    ):
    """
    Get news.
    """
    news = db.query(News).filter(News.category == category).all()
    
    return paginate(res=news,pagination=pagination)
