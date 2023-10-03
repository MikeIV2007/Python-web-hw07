from src.db import session
from src.models import Student


def create_teacher(name):
    teacher = Student(fullname=name)
    session.add(teacher)
    session.commit()
    session.close()
    print(f"New teacher with name {name} created")


def list_teachers():
    teachers = session.query(Student).all()
    print("List of teachers")
    return teachers


def update_teacher(id, new_name):
    teacher = session.query(Student).filter(Student.id == id)
    teacher.update({"fullname": new_name})
    session.commit()
    session.close()
    print(f"Name of teacher with id {id} renewed. New name: {new_name}")
    return teacher.one()


def remove_teacher(id):
    r = session.query(Student).filter(Student.id == id).delete()
    session.commit()
    session.close()
    print(f"Teacher with id {id} removed")
    return r
