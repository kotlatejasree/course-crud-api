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