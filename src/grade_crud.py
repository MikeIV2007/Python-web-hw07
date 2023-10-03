from datetime import datetime
from random import choice

from sqlalchemy import select

from src.db import session
from src.models import Grade, Student, Discipline
from seed import date_range




def create_grade(name):
    start_date = datetime.strptime("2023-09-01", "%Y-%m-%d")
    print(start_date)
    end_date = datetime.strptime("2024-06-20", "%Y-%m-%d")
    list_of_dates = date_range(start=start_date, end=end_date)
    students_ids = session.scalars(select(Student.id)).all()
    disciplines_ids = session.scalars(select(Discipline.id)).all()
    grade = Grade(grade=int(name), student_id=choice(students_ids), discipline_id=choice(disciplines_ids), date_of=choice(list_of_dates))
    session.add(grade)
    session.commit()
    session.close()
    print(f"New grade {name} created.")


def list_grades():
    grades = session.query(Grade).all()
    print("List of grades")
    return grades


def update_grade(id, new_grade):
    grade = session.query(Grade).filter(Grade.id == id)
    grade.update({"grade": new_grade})
    session.commit()
    session.close()
    print(f"Grade with id {id} renewed. New grade: {new_grade}")
    return grade.one()


def remove_grade(id):
    r = session.query(Grade).filter(Grade.id == id).delete()
    session.commit()
    session.close()
    print(f"Grade with id {id} removed")
    return r
