class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, [grade])
        else:
            return 'Ошибка'

    def average_mark(self):
        if len(self.grades.values()) > 0:
            all_marks_list = sum(self.grades.values(), [])
            return round(sum(all_marks_list) / len(all_marks_list), 1)
        else:
            return 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_mark()}\n'
                f'Курсы в процессе изучения: {', '.join(set(self.courses_in_progress))}\n'
                f'Завершенные курсы: {', '.join(set(self.finished_courses))}')

    def __eq__(self, other):
        return self.average_mark() == other.average_mark()

    def __gt__(self, other):
        return self.average_mark() > other.average_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_mark(self):
        if len(list(self.grades.values())) > 0:
            all_marks_list = sum(self.grades.values(), [])
            return round(sum(all_marks_list) / len(all_marks_list), 1)
        else:
            return 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_mark()}')

    def __eq__(self, other):
        return self.average_mark() == other.average_mark()

    def __gt__(self, other):
        return  self.average_mark() > other.average_mark()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def average_mark_students(students_list, course):
    """
    Function count average mark of list of students
    :param students_list: list of students
    :param course: course name
    :return: average mark
    """
    marks_list = []
    for student in students_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            marks_list.append(student.grades.get(course))
    if len(marks_list) > 0:
        all_marks_list = sum(marks_list, [])
        return round(sum(all_marks_list) / len(all_marks_list), 1)
    else:
        return 0


def average_mark_lecturers(lecturers_list, course):
    """
    Function count average mark of list of lecturers
    :param lecturers_list: list of lecturers
    :param course: course name
    :return: average mark
    """
    marks_list = []

    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            marks_list.append(lecturer.grades.get(course))

    if len(marks_list) > 0:
        all_marks_list = sum(marks_list, [])
        return round(sum(all_marks_list) / len(all_marks_list), 1)
    else:
        return 0


# Проверка к задаче
print('Проверка к задаче:', '====================', sep='\n')
some_reviewer = Reviewer('Some', 'Reviewer')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Java']
some_reviewer_1 = Reviewer('Other', 'Reviewer')
print(some_reviewer, end='\n\n')
print(some_reviewer_1, end='\n\n')

some_student = Student('Some', 'Student', 'М')
some_student.courses_in_progress += ['Python', 'Java']
some_student.finished_courses += ['Введение в программирование']
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 3)
some_reviewer.rate_hw(some_student, 'Java', 10)
some_student_1 = Student('Other', 'Student', 'Ж')
some_student_1.courses_in_progress += ['Python']
some_reviewer.rate_hw(some_student_1, 'Python', 8)
print(some_student, end='\n\n')
print(some_student_1, end='\n\n')
print(some_student == some_student_1, end='\n\n')
print(some_student > some_student_1, end='\n\n')
print(some_student < some_student_1, end='\n\n')

some_lecturer = Lecturer('Some', 'Lecturer')
some_lecturer.courses_attached += ['Python', 'Java']
some_lecturer_1 = Lecturer('Other', 'Lecturer')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_2 = Lecturer('Another', 'Lecturer')
some_lecturer_2.courses_attached += ['Java']
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Java', 4)
some_student.rate_lecture(some_lecturer_1, 'Python', 8)

print(some_lecturer, end='\n\n')
print(some_lecturer_1, end='\n\n')

print(some_lecturer == some_lecturer_1, end='\n\n')
print(some_lecturer > some_lecturer_2, end='\n\n')
print(some_student < some_student_1, end='\n\n')

students_list = [some_student, some_student_1]
print(average_mark_students(students_list, 'Python'))

lecturers_list = [some_lecturer,some_lecturer_1, some_lecturer_2]
print(average_mark_lecturers(lecturers_list, 'Python'))