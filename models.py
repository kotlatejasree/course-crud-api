from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Course(Base):
    __tablename__="courses"

    id=Column(Integer,index=True,primary_key=True)
    name=Column(String(50),nullable=False)
    instructor=Column(String(50),nullable=False)
    fee=Column(Integer,nullable=False)

class Student(Base):
    __tablename__="students"

    id=Column(Integer,index=True,primary_key=True)
    name=Column(String(50),nullable=False)
    course_id=Column(Integer,nullable=False)
    hashed_password=Column(String(400),nullable=False)
    is_admin=Column(Boolean,default=False,nullable=False)
    is_active=Column(Boolean,default=True,nullable=False)
    email=Column(String(50),nullable=False,unique=True)