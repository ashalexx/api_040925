from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


# @app.get("/students")
# def get_all_students():
#     return json_to_dict_list(path_to_json)

# параметр запроса
@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list


# параметр пути
# @app.get("/students/{course}")
# def get_all_students_course(course: int):
#     students = json_to_dict_list(path_to_json)
#     return_list = []
#     for student in students:
#         if student["course"] == course:
#             return_list.append(student)
#     return return_list

# пример комбинации параметров пути и параметров запроса
@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students


@app.get("/students/{student_id}")
def get_all_student_from_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student["student_id"] == student_id:
            return_list.append(student)
    return return_list


@app.get("/student")
def get_student_from_param_id(student_id: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if student_id is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["student_id"] == student_id:
                return_list.append(student)
        return return_list
