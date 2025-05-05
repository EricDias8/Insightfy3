from sqlalchemy import Column, Integer, String
from .database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String)
    summary = Column(String)
    category = Column(String)
    label = Column(String)
