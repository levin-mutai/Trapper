from fastapi import BackgroundTasks, Depends, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.utils import response
from database import get_db
from routers.news import router as news
from database import Engine
import models.models as models
from config.settings import DEBUG,ORIGINS
from deps.pagination import get_pagination
from utils.utils import paginate
from sqlalchemy.orm import Session
from models.models import News
from schemas.schemas import News as NewsSchema

import auth


# to create all the tables using the already defined schema
models.Base.metadata.create_all(bind=Engine) # type: ignore

app = FastAPI(debug=DEBUG, title="Trapper News API", version="0.1.0")

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news)



@app.get("/news")
def get_news(
    source:str = Query("",description="Get news from specic Source eg. cnn or aljazeera"), 
    pagination:dict = Depends(get_pagination),
    db: Session = Depends(
        get_db,
    ),
    ):
    """
    Used to get all the news from the database. <br/>
    :param source: str <br/>
    :param skip: int  <br/>
    :param limit: int <br/>
    :param total_items: int <br/>
    :return: list of all the available  news. <br/>
    """
    if source:
        news = db.query(News).filter(News.source == source).all()
        return paginate(res=news,pagination=pagination)  
    
    news = db.query(News).all()
    
    return paginate(res=news,pagination=pagination)  

@app.get("/news/{category}")
def get_news_by_category(
    category:str,
    source:str = Query("",description="Get news from specic Source eg. cnn or aljazeera"), 
    pagination:dict = Depends(get_pagination),
    db: Session = Depends(
        get_db,
    ),
    ):
    """
    used to filter news by categories from the system. <br/>
    :param category: str <br/>
    :param skip: int  <br/>
    :param limit: int <br/>
    :param total_items: int <br/>
    :return: list of all the available  news. <br/>
    """
    if source:
        news = db.query(News).filter(News.category.ilike(f"%{category}%"),News.source == source).all()
        return paginate(res=news,pagination=pagination)

    news = db.query(News).filter(News.category.ilike(f"%{category}%")).all()
    
    return paginate(res=news,pagination=pagination)
@app.get("/categories")
def get_category(
    db: Session = Depends(
        get_db,
    ),
    ):
    """
    Used to get all the news category from the database. <br/>
    :return: list of all the available categories. <br/>
    """

    
    categories = db.query(News.category).distinct().all() # type: ignore
    
    return response(res=[category[0] for category in categories])
  


@app.get("/sources")
def get_sources(
    db: Session = Depends(
        get_db,
    ),
    ):
    """
    Returns All the News Sources Collected.
    """
    sources = db.query(News.source).distinct().all() 
    
    return response(res=[source[0] for source in sources])
