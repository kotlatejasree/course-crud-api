from sqlalchemy.orm import Session
import models 
import schemas

def create_course(db:Session,course:schemas.CourseCreate):
    db_course=models.Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db:Session):
    return db.query(models.Course).all()

def get_course(db:Session,course_id:int):
    return db.query(models.Course).filter(
        models.Course.id==course_id
        ).first()

def delete_course(db: Session, course_id: int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        return False
    db.delete(course)
    db.commit()
    return True

def update_course(db:Session,course_id:int,course:schemas.CourseCreate):
    db_course=get_course(db,course_id)
    if not db_course:
        return None 
    db_course.name=course.name
    db_course.instructor=course.instructor
    db_course.fee=course.fee  
    db.commit()
    db.refresh(db_course)
    return db_course


def put_course(db:Session,course_id:int,course:schemas.CourseCreate):
    db_course=get_course(db,course_id)
    if not db_course:
        return None 
    db_course.id=course.id
    db_course.name=course.name  
    db_course.instructor=course.instructor
    db_course.fee=course.fee  
    db.commit()
    db.refresh(db_course)
    return db_course


def get_courses_by_name(db: Session, course_name: str):
    return db.query(models.Course).filter(
        models.Course.name == course_name
    ).all()

