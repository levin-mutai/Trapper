from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    BackgroundTasks
)
from api.src.deps.pagination import get_pagination

from api.src.utils.utils import paginate, response



background_tasks = BackgroundTasks()

router = APIRouter(tags=["Wallet"], prefix="")

router.get("/")
def get_news(
    background_tasks: BackgroundTasks,
    pagination:dict = Depends(get_pagination)):
    """
    Get news.
    """
    return paginate(res="res",pagination=pagination)  
router.get("/categories")
def get_category(
    background_tasks: BackgroundTasks,
    pagination:dict = Depends(get_pagination)):
    """
    Get news.
    """
    return response(res="res")    
router.get("/categories/{category}")
def get_news_by_category(
    background_tasks: BackgroundTasks,
    pagination:dict = Depends(get_pagination)):
    """
    Get news.
    """
    return paginate(res="res",pagination=pagination)
