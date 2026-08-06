from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__="courses"

    id=Column(Integer,index=True,primary_key=True)
    name=Column(String(50),nullable=False)
    instructor=Column(String(50),nullable=False)
    fee=Column(Integer,nullable=False)

