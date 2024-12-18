from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    sender = Column(String, nullable=True)
    platform = Column(String, nullable=True)
    timestamp = Column(DateTime, nullable=True)
