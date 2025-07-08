from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True) 
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)