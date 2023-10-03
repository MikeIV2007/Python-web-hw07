from sqlalchemy import and_
from src.db import session
import argparse

from src.teacher_crud import create_teacher, list_teachers, update_teacher, remove_teacher
from src.groupe_crud import create_group, list_groups, update_group, remove_group
from src.student_crud import create_student, list_students, update_student, remove_student
from src.discipline_crud import create_discipline, list_disciplines, update_discipline, remove_discipline
from src.grade_crud import create_grade, list_grades, update_grade, remove_grade

def main():
    parser = argparse.ArgumentParser(description="CLI програма для CRUD операцій із базою даних")

    parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"], required=True, help="Command: create, list, update або remove")
    parser.add_argument("--model", "-m", choices=["Teacher", "Group", "Student", "Discipline", "Grade"], required=True, help="Model: Teacher Group, Student, Discipline, Grade")
    parser.add_argument("--id", type=int, help="ID of model for updating or removing")
    parser.add_argument("--name", "-n", help="Name of model for creating or updating /from 1-12 number string for module Grade")

    args = parser.parse_args()
    
    if args.model == "Teacher":
        match args.action:
            case 'create':
                create_teacher (args.name)
            case 'list':
                teachers = list_teachers()
                for t in teachers:
                    print(t.id, t.fullname)
            case 'update':
                t = update_teacher(args.id, args.name)
                if t:
                    print('Successfully')
                else:
                    print(f"Teacher with name {args.name} not found")
            case 'remove':
                r = remove_teacher(args.id)
                if r:
                    print('Successfully')
                else:
                    print(f"Teacher with id {args.id} not found")                    
            case _:
                print (f"Command {args.model} not exist")

    if args.model == "Group":
        match args.action:
            case 'create':
                create_group (args.name)
            case 'list':
                groups = list_groups()
                for g in groups:
                    print(g.id, g.name)
            case 'update':
                t = update_group(args.id, args.name)
                if t:
                    print('Successfully')
                else:
                    print(f"Grope with name {args.name} not found")
            case 'remove':
                r = remove_group(args.id)
                if r:
                    print('Successfully')
                else:
                    print(f"Grope with id {args.id} not found")                    
            case _:
                print (f"Command {args.model} not exist")

    if args.model == "Student":
        match args.action:
            case 'create':
                create_student(args.name)
            case 'list':
                students = list_students()
                for s in students:
                    print(s.id, s.fullname)
            case 'update':
                t = update_student(args.id, args.name)
                if t:
                    print('Successfully')
                else:
                    print(f"Student with name {args.name} not found")
            case 'remove':
                r = remove_student(args.id)
                if r:
                    print('Successfully')
                else:
                    print(f"Student with id {args.id} not found")                    
            case _:
                print (f"Command {args.model} not exist")

    if args.model == "Discipline":
        match args.action:
            case 'create':
                create_discipline(args.name)
            case 'list':
                disciplines = list_disciplines()
                for s in disciplines:
                    print(s.id, s.name)
            case 'update':
                t = update_discipline(args.id, args.name)
                if t:
                    print('Successfully')
                else:
                    print(f"Discipline with name {args.name} not found")
            case 'remove':
                r = remove_discipline(args.id)
                if r:
                    print('Successfully')
                else:
                    print(f"Discipline with id {args.id} not found")                    
            case _:
                print (f"Command {args.model} not exist")


    if args.model == "Grade":
        match args.action:
            case 'create':
                create_grade(args.name)
            case 'list':
                grades = list_grades()
                for g in grades:
                    print(g.id, g.grade, g.date_of, g.student.fullname, g.discipline.name)
            case 'update':
                t = update_grade(args.id, args.name)
                if t:
                    print('Successfully')
                else:
                    print(f"Grade with name {args.name} not found")
            case 'remove':
                r = remove_grade(args.id)
                if r:
                    print('Successfully')
                else:
                    print(f"Grade with id {args.id} not found")                    
            case _:
                print (f"Command {args.model} not exist")

if __name__ == "__main__":
    main()
