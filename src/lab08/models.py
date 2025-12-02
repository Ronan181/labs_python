from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str  
    group: str
    gpa: float       

    # Валидация
    def __post_init__(self):
        # корректный формат даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("birthdate must be in format YYYY-MM-DD")
        # gpa 0–5
        if not (0 <= self.gpa <= 5):
            raise ValueError()

    # Возраст
    def age(self) -> int:
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    # Сериализация
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    # Десериализация
    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"],
        )
    
    def __str__(self):
        return f" Студент: {self.fio}, группа {self.group}, GPA {self.gpa}, возраст {self.age()}"

s = Student(fio="Иванов Петр", birthdate="2007-10-19", group="BIVT-25-8", gpa=4.8)
print(s)