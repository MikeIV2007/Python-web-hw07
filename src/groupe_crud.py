from src.db import session
from src.models import Group

def create_group(name):
    group = Group(name = name)
    session.add(group)
    session.commit()
    session.close()
    print(f"New grope with name {name} created")


def list_groups():
    teachers = session.query(Group).all()
    print("List of groups")
    return teachers
    

def update_group(id, new_name):
    group = session.query(Group).filter(Group.id == id)
    group.update({'name': new_name})
    session.commit()
    session.close()
    print(f"Name of group with id {id} renewed. New name: {new_name}")
    return group.one()
    

def remove_group(id):
    r = session.query(Group).filter(Group.id == id).delete()
    session.commit()
    session.close()
    print(f"Group with id {id} removed")
    return r 
    