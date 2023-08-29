from database import Base

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    headline  = Column(String)
    link = Column(String)
    postdate = Column(DateTime)
    category = Column(String)
    # content = Column(String, nullable=True)
    source = Column(String)