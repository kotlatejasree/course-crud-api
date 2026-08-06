from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import crud,schemas
from database import Base,engine,sessionlocal
from typing import List
Base.metadata.create_all(bind=engine)


app=FastAPI()
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def welcome():
    return {"message":"Welcome to the course registration portal"}        


@app.post("/courses/",response_model=schemas.CourseResponse)
def create(course:schemas.CourseCreate,db:Session=Depends(get_db)):
    return crud.create_course(db,course)

@app.get("/courses/",response_model=List[schemas.CourseResponse])
def read_all(db:Session = Depends(get_db)):
    return crud.get_courses(db)


@app.get("/course/{course_id}", response_model=schemas.CourseResponse)
def read_one(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.put("/courses/{course_id}",response_model=schemas.CourseResponse)
def update(course_id:int,course:schemas.CourseCreate,db:Session=Depends(get_db)):
    db_course=crud.update_course(db,course_id,course)
    if db_course is None:
        raise HTTPException(status_code=404,detail="Course not found")
    return db_course

@app.delete("/courses/{course_id}")
def delete(course_id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_course(db,course_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Course not found") 
    return {"message":"Course deleted successfully"}


@app.get("/courses/name/{course_name}")
def get_courses_by_name(course_name:str,db:Session=Depends(get_db)):
    courses_list=crud.get_courses_by_name(db,course_name)
    if not courses_list:
        raise HTTPException(status_code=404,detail="No courses found for the specified name")
    return courses_list

