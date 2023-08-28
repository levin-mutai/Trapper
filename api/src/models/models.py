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

    # def __init__(self, title, url, date, category, content, source):
    #     self.title = title
    #     self.url = url
    #     self.date = date
    #     self.category = category
    #     self.content = content
    #     self.source = source

    # def __repr__(self):
    #     return "<News(title='%s', url='%s', date='%s', category='%s', content='%s', source='%s')>" % (
    #         self.title, self.url, self.date, self.category, self.content, self.source)