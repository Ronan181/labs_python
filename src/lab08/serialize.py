import json
from models import Student
from pathlib import Path
import sys
import os
sys.path.append('/Users/ars/Documents/GitHub/labs_python/src/lab08/')

from models import *

students=[Student(fio="Иванов Петр", birthdate="2007-10-19", group="BIVT-25-8", gpa=4.8),
          Student(fio="Петров Иван", birthdate="2006-09-28", group="BIVT-25-12", gpa=4.6),]

def students_to_json(students, path):
    # Сохраняет список Student в JSON-файл
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path) -> list[Student]:
    # Загружает список Student из JSON-файла
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError()

    students = []
    for item in data:
        # Проверка, что item — словарь
        if not isinstance(item, dict):
            raise ValueError()
        # Проверка обязательных полей
        required = ["fio", "birthdate", "group", "gpa"]
        for key in required:
            if key not in item:
                raise ValueError()
        # Создаём объект Student (валидация произойдёт в классе)
        students.append(Student.from_dict(item))
    return students

base_dir = Path("/Users/ars/Documents/GitHub/labs_python")
json_path = base_dir / "data" / "lab08" / "students_input.json"

students_to_json(students, json_path)
print(students_from_json(json_path))
