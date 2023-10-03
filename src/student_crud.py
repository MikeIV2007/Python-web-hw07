from src.db import session
from src.models import Student, Group
from random import randint, choice
from sqlalchemy import select


def create_student(name):
    group_ids = session.scalars(select(Group.id)).all()
    student = Student(fullname=name, group_id=choice(group_ids))
    session.add(student)
    session.commit()
    session.close()
    print(f"New student with name {name} created.")


def list_students():
    students = session.query(Student).all()
    print("List of students")
    return students


def update_student(id, new_name):
    student = session.query(Student).filter(Student.id == id)
    student.update({"fullname": new_name})
    session.commit()
    session.close()
    print(f"Name of student with id {id} renewed. New name: {new_name}")
    return student.one()


def remove_student(id):
    r = session.query(Student).filter(Student.id == id).delete()
    session.commit()
    session.close()
    print(f"Student with id {id} removed")
    return r
