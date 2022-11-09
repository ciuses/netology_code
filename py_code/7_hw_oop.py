# class Students:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.closed_courses = []


# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]
#
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def add_courses(self, course_name):
#         self.finished_courses.append(course_name)
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def put_two(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress:

            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        if not self.grades:
            return 0

        estimations = []
        for estimation in self.grades.values():
            estimations.extend(estimation)

        return sum(estimations) / len(estimations)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.average_rating()}\n' \
               f'Курсы в процесе изучения: {self.courses_in_progress}\n' \
               f'Завершённые курсы: {self.finished_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def average_rating(self):
        if not self.lecturer_grades:
            return 0

        estimations = []
        for estimation in self.lecturer_grades.values():
            estimations.extend(estimation)

        return sum(estimations) / len(estimations)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_rating()}'


# '''создание студента и назначение ему курса'''
# best_student = Student('Михаил', 'Ломоносов', 'male')
# best_student.courses_in_progress += ['Python']
#
# '''создание создание ревьюера и назначение для него курса'''
# cool_mentor = Reviewer('СуперПрепод', 'Гениев')
# cool_mentor.courses_attached += ['Python']
#
# '''оценка студента ревьюером'''
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)
# print(dir(cool_mentor))
# print(cool_mentor.__dict__)

'''создание студента и назначение ему курса'''
another_student = Student('Студентка', 'Клёвая', 'female')
another_student.courses_in_progress += ['Баньщики']
#
# '''создание лектора и назначение курса'''
# another_lecturer = Lecturer('Мария Ивановна', 'Иванова')
# another_lecturer.courses_attached += ['Баньщики']
#
# '''блок оценки лектора судентом'''
# another_student.put_two(another_lecturer, 'Баньщики', 2)
# another_student.put_two(another_lecturer, 'Баньщики', 7)
# another_student.put_two(another_lecturer, 'Баньщики', 5)
#
'''блок добавления оценок и лекций студенту'''
another_student.grades['Python'] = [3, 6, 9]
another_student.grades['Ruby'] = [1, 1, 1]
another_student.grades['Java'] = [1, 1, 1]
another_student.courses_in_progress += ['Python']
another_student.courses_in_progress += ['Ruby']
another_student.courses_in_progress += ['Java']
another_student.finished_courses += ['Повар']

# print(another_lecturer.lecturer_grades)

# print(cool_mentor)
# print(another_lecturer)
print(another_student)


# sokrat = Lecturer('Сократ', 'Философов')
# sokrat.lecturer_grades['Философия'] = [1, 1, 1]
# sokrat.lecturer_grades['Пьянство'] = [2, 2, 2]
# sokrat.lecturer_grades['История'] = [3, 3, 3]
#
# print(sokrat)


