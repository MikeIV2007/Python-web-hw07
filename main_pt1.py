from sqlalchemy import func, desc, select, and_

from src.models import Student, Teacher, Discipline, Grade, Group
from src.db import session


def select_1():
    """
    --Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
        SELECT s.fullname AS Students, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        GROUP BY s.fullname
        ORDER BY avg_grade DESC
        LIMIT 5;
    """
    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


def select_2(discipline_id: int):
    """
    --Знайти студента із найвищим середнім балом з певного предмета.
        SELECT s.fullname AS Student, d.name AS Discipline, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN disciplines d ON d.id  = g.discipline_id
        WHERE d.id  = 2
        GROUP BY s.fullname
        ORDER BY avg_grade DESC
        LIMIT 1;
    """
    result = (
        session.query(
            Discipline.name,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return result


def select_3(discipline_id: int):
    """
    Знайти середній бал у групах з певного предмета.
        SELECT d.name AS Disciplines, gr.name AS Groups, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN disciplines d ON d.id  = g.discipline_id
        LEFT JOIN [groups] gr ON gr.id  = s.group_id
        WHERE d.id  = 7
        GROUP BY gr.name, d.name
        ORDER BY avg_grade DESC;
    """
    result = (
        session.query(
            Discipline.name.label("Disciplines"),
            Group.name.label("Groups"),
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .where(Discipline.id == discipline_id)
        .group_by(Group.name, Discipline.name)
        .order_by(func.avg(Grade.grade).desc())
        .all()
    )
    return result


def select_4():
    """
    --Знайти середній бал на потоці (по всій таблиці оцінок).
        SELECT ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
    """
    result = (
        session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .select_from(Grade)
        .all()
    )
    return result


def select_5(teacher_id: int):
    """
    --Знайти які курси читає певний викладач.
        SELECT  d.name AS Discipline_name, t.fullname AS Teacher_name
        FROM disciplines d
        JOIN teachers t  ON t.id  = d.teacher_id
        WHERE t.id  = 5
        ORDER BY d.name;
    """
    result = (
        session.query(
            Discipline.name.label("Disciplines"),
            Teacher.fullname.label("Tacher"),
        )
        .select_from(Discipline)
        .join(Teacher)
        .where(Teacher.id == teacher_id)
        .order_by(Discipline.name)
        .all()
        )
    return result


def select_6(group_id: int):
    """
    --Знайти список студентів у певній групі.
        SELECT s.fullname  AS Students, gr.name  AS Group_name
        FROM students s
        LEFT JOIN [groups] gr ON gr.id  = s.group_id
        WHERE gr.id = 3
        ORDER BY s.fullname;
    """
    result = (
        session.query(
            Student.fullname.label("Students"),
            Group.name.label("Group"),
        )
        .select_from(Student)
        .join(Group)
        .where(Group.id == group_id)
        .order_by(Student.fullname)
        .all()
    )
    return result


def select_7(discepline_id: int, group_id: int):
    """
    --Знайти оцінки студентів у окремій групі з певного предмета.
        SELECT s.fullname  AS Students, gr.name AS Group_name, d.name AS Discipline, g.grade AS Grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN disciplines d ON d.id  = g.discipline_id
        LEFT JOIN [groups] gr ON gr.id  = s.group_id
        WHERE d.id  = 6 AND gr.id = 3
        GROUP BY s.fullname
        ORDER BY s.fullname;
    """
    result = (
        session.query(
            Student.fullname.label("Students"),
            Group.name.label("Group"),
            Discipline.name.label("Discipline"),
            Grade.grade.label("Grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .where(Discipline.id == discepline_id, Group.id == group_id)
        .order_by(Student.fullname)
        .all()
    )
    return result


def select_8(teacher_id: int):
    """
    --Знайти середній бал, який ставить певний викладач зі своїх предметів.
        SELECT t.fullname  AS Teacher, d.name AS Discipline, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN disciplines d ON d.id  = g.discipline_id
        LEFT JOIN teachers t ON t.id = d.teacher_id
        WHERE d.teacher_id = 4
        GROUP BY g.discipline_id
        ORDER BY d.name;
    """
    result = (
        session.query(
            Student.fullname.label("Teacher"),
            Discipline.name.label("Discipline"),
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .where(Student.id == teacher_id)
        .group_by(Student.fullname, Discipline.name)
        .all()
    )
    return result


def select_9(student_id: int):
    """
    --Знайти список курсів, які відвідує студент.
        SELECT d.name AS Discipline, s.fullname  AS Student
        FROM disciplines d
        LEFT JOIN grades g  ON g.discipline_id  = d.id
        LEFT JOIN students s ON s.id = g.student_id
        WHERE s.id  = 6
        GROUP BY d.name
        ORDER BY d.name;
    """
    result = (
        session.query(
            Discipline.name.label("Discipline"),
            Student.fullname.label("Student"),
        )
        .select_from(Discipline)
        .join(Grade)
        .join(Student)
        .where(Student.id == student_id)
        .group_by(Discipline.name, Student.fullname)
        .order_by(Discipline.name)
        .all()
    )
    return result


def select_10(student_id, teacher_id):
    """
    --Список курсів, які певному студенту читає певний викладач.
        SELECT d.name AS Discipline, s.fullname AS Students, t.fullname AS Teacher
        FROM disciplines d
        JOIN grades g  ON g.discipline_id  = d.id
        JOIN students s ON s.id = g.student_id
        JOIN teachers t ON t.id = d.teacher_id
        WHERE s.id  = 45 AND t.id = 2
        GROUP BY d.name, s.fullname, t.fullname
        ORDER BY d.name;
    """
    result = (
        session.query(
            Discipline.name.label("Discipline"),
            Student.fullname.label("Student"),
            Teacher.fullname.label("Teacher"),
        )
        .select_from(Discipline)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .where(Student.id == student_id, Teacher.id == teacher_id)
        .group_by(Discipline.name, Student.fullname, Teacher.fullname)
        .order_by(Discipline.name)
        .all()
    )
    return result


def select_11(teacher_id: int, student_id: int):
    """
    --Середній бал, який певний викладач ставить певному студентові.
        SELECT t.fullname AS Teacher, s.fullname AS Student, ROUND(AVG(g.grade), 2) AS avg_grade
        FROM grades g
        JOIN students s ON s.id = g.student_id
        JOIN disciplines d ON d.id = g.discipline_id
        JOIN teachers t ON t.id = d.teacher_id
        WHERE t.id = 2 AND s.id = 30
        GROUP BY t.fullname, s.fullname
    """
    result = (
        session.query(
            Teacher.fullname.label("Teacher"),
            Student.fullname.label("Student"),
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .join(Student)
        .join(Discipline)
        .join(Teacher)
        .where(Teacher.id == teacher_id, Student.id == student_id)
        .group_by(Teacher.fullname, Student.fullname)
        .all()
    )
    return result


def select_12(discipline_id, group_id):
    """
    --Оцінки студентів у певній групі з певного предмета на останньому занятті.
        SELECT s.id, s.fullname, g.grade, g.date_of
        FRON grades g
        INNER JOIN students s on s.id = g.student_id
        WHERE g.discipline_id = 2
        AND s.group_id = 2
        AND g.date_of = (select max(date_of) -- находим последнее занятие для данной группы по данному предмету
            FROM grades g2
            INNER JOIN students s2 on s2.id = g2.student_id
            WHERE g2.discipline_id = g.discipline_id
            AND s2.group_id = s.group_id);
    """
    subquery = (
        select(Grade.date_of)
        .join(Student)
        .join(Group)
        .where(and_(Grade.discipline_id == discipline_id, Group.id == group_id))
        .order_by(desc(Grade.date_of))
        .limit(1)
        .scalar_subquery()
    )

    r = (
        session.query(
            Discipline.name, Student.fullname, Group.name, Grade.date_of, Grade.grade
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(
            and_(
                Discipline.id == discipline_id,
                Group.id == group_id,
                Grade.date_of == subquery,
            )
        )
        .order_by(desc(Grade.date_of))
        .all()
    )
    return r


if __name__ == "__main__":
    #print(select_1())
    #print(select_2(1))
    #print (select_3(1))
    #print (select_4())
    #print (select_5(5))
    #print (select_6(3))
    #print (select_7(2, 3))
    #print (select_8(5))
    #print (select_9(20))
    #print (select_10(20, 3))
    #print(select_11(2, 2))
    print(select_12(1, 2))
