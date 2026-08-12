from pydantic import BaseModel

class CourseCreate(BaseModel):
    id:int
    name:str
    instructor:str
    fee:int

class CourseResponse(CourseCreate):
    id:int

    model_config={
        "from_attributes":True
    }

class Student(BaseModel):
    id:int
    name:str
    email:str
class Studentlogin(BaseModel):
    email:str
    password:str
    
class StudentResponse(Student):
    id:int
    name:str
    email:str

    model_config={
        "from_attributes":True
    }