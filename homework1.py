class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        if not self.grades:
            return 0
        return round(sum(grade for grades in self.grades.values() for grade in grades) /
                     sum(len(grades) for grades in self.grades.values()), 1)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.get_avg_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не могу сравнивать с не студентами!')
            return
        return self.get_avg_grade() < other.get_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        if not self.grades:
            return 0
        return round(sum(grade for grades in self.grades.values() for grade in grades) /
                     sum(len(grades) for grades in self.grades.values()), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не могу сравнивать с не лекторами!')
            return
        return self.get_avg_grade() < other.get_avg_grade()


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached.append('Python')

cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached.append('Python')

# Оценки по д3
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

# Оценки лектора
best_student.rate_lecture(cool_lecturer, 'Python', 9)

# Вывод информации
print(best_student)
print(cool_reviewer)
print(cool_lecturer)

# Пример сравнения
new_student = Student('John', 'Doe', 'your_gender')
print(best_student < new_student)  # Сравнение студентов
new_lecturer = Lecturer('Petr', 'Petrov')
print(cool_lecturer < new_lecturer)  # Сравнение лекторов

# Функции для средней оценки
def average_grade_for_students(students, course):
    total_grade = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grade / total_students if total_students > 0 else 0

def average_grade_for_lecturers(lecturers, course):
    total_grade = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    return total_grade / total_lecturers if total_lecturers > 0 else 0

# Подсчет средней оценки студентов и лекторов по курсу Python
students = [best_student]
lecturers = [cool_lecturer]

average_student_grade = average_grade_for_students(students, 'Python')
average_lecturer_grade = average_grade_for_lecturers(lecturers, 'Python')

print(f'Средняя оценка студентов за курс Python: {average_student_grade}')
print(f'Средняя оценка лекторов за курс Python: {average_lecturer_grade}')