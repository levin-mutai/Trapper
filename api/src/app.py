from fastapi import BackgroundTasks, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from routers.news import router as news
from database import Engine
import models.models as models
from config.settings import DEBUG,ORIGINS
from deps.pagination import get_pagination
from utils.utils import paginate
from sqlalchemy.orm import Session
from models.models import News

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




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/news")
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