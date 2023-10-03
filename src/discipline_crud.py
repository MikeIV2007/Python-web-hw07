from src.db import session
from src.models import Teacher, Discipline
from random import randint, choice
from sqlalchemy import select


def create_discipline(name):
    teachers_ids = session.scalars(select(Teacher.id)).all()
    discipline = Discipline(name=name, teacher_id=choice(teachers_ids))
    session.add(discipline)
    session.commit()
    session.close()
    print(f"New discipline with name {name} created.")


def list_disciplines():
    disciplines = session.query(Discipline).all()
    print("List of disciplines")
    return disciplines


def update_discipline(id, new_name):
    discipline = session.query(Discipline).filter(Discipline.id == id)
    discipline.update({"name": new_name})
    session.commit()
    session.close()
    print(f"Name of discipline with id {id} renewed. New name: {new_name}")
    return discipline.one()


def remove_discipline(id):
    r = session.query(Discipline).filter(Discipline.id == id).delete()
    session.commit()
    session.close()
    print(f"Discipline with id {id} removed")
    return r
