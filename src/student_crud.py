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

    # ----Retrieve all existing group ids
    # group_ids = session.query(Group.id).all()


    # if not group_ids:
    #     print("No groups exist. Please create groups before adding students.")
    #     return

    # # Randomly select a group id
    # selected_group_id = choice(group_ids)[0]

    # # Create a new student with the selected group id
    # student = Student(fullname=name, group_id=selected_group_id)

    # try:
    #     # Add the student to the session and commit the transaction
    #     session.add(student)
    #     session.commit()
    #     print(f"New student with name {name} and group_id {selected_group_id} created.")
    # except Exception as e:
    #     # Handle any exceptions that may occur during the transaction
    #     session.rollback()
    #     print(f"Error creating student: {str(e)}")
    # finally:
    #     # Close the session
    #     session.close()


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
