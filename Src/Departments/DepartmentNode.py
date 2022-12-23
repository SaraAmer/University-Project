from Src.Courses.CoursesNode import CourseNode
from Src.Students.StudentNode import StudentNode
from Src.Courses.Courses import Courses
from Src.Students.Students import Student
from Src.StudentCourses.SudentCourses import StudentCourses
from Src.Helper import CommnFunctions


class DepartmentNode:

    def __init__(self, data):
        self.__code = data['code']
        self.__name = data['name']
        self.__number = data['number']
        self.__college = None
        self.__next_node = None
        self.__previous_node = None
        self.__students = None
        self.__next_department = None
        self.__courses = None

    def set_code(self, code):
        self.__code = code

    def get_code(self):
        return self.__code

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_college(self, college):
        self.__college = college

    def get_college(self):
        return self.__college

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    def get_next_department(self):
        return self.__next_department

    def set_next_department(self, next_department):
        self.__next_department = next_department

    def get_courses(self):
        return self.__courses

    def set_courses(self, courses):
        self.__courses = courses

    @staticmethod
    def get_user_department_data():
        course_data = {
            'name': input("Enter the department Name: "),
            'code': input("Enter the department code: "),
            'number': input("Enter the department number: ")
        }
        return course_data

    def update_department_data(self, data):
        self.set_name(data['name'])
        self.set_number(data['number'])
        self.set_code(data['code'])

    def update_department(self):
        course_new_data = self.get_user_department_data()
        self.update_department_data(course_new_data)

    def get_last_course(self):
        temp = self.__courses
        if temp is None:
            return temp
        while temp.get_next_node() is not None:
            temp = temp.get_next_node()
        return temp

    def add_course(self):
        last_course = self.get_last_course()
        new_course_data = CourseNode.get_user_course_data()
        new_course = CourseNode(new_course_data)
        new_course.set_department(self)
        if last_course is None:
            self.__courses = new_course
        else:
            last_course.set_next_node(new_course)

    def print_department_courses(self):
        temp = self.__courses
        while temp is not None:
            print(temp.get_code() + ")" + temp.get_name())
            temp = temp.get_next_node()

    def get_last_student(self):
        temp = self.__students
        if temp is None:
            return temp
        while temp.get_next_node() is not None:
            temp = temp.get_next_node()
        return temp

    def add_student(self):
        last_student = self.get_last_student()
        new_student_data = StudentNode.get_user_student_data()
        new_student = StudentNode(new_student_data)
        new_student.set_department(self)
        print(new_student.get_department())
        if last_student is None:
            self.__students = new_student
        else:
            last_student.set_next_node(new_student)

    def print_department_students(self):
        temp = self.__students
        while temp is not None:
            print(temp.get_id() + ")" + temp.get_name())
            temp = temp.get_next_node()

    def update_department_course(self):
        Courses.update_course(self.__courses)

    def delete_department_course(self):
        Courses.delete_course(self.__courses)

    def update_department_student(self):
        Student.update_student(self.__students)

    def delete_department_student(self):
        Student.delete_student(self.__students)

    def assign_course_to_student(self):
        StudentCourses.assign_student_to_course(self.__courses, self.__students)

    def print_course_students(self):
        Courses.print_course_students(self.__courses)

    def print_student_courses(self):
        Student.print_student_courses(self.__students)

    def department_option(self):
        choice = 0
        while choice != 12:
            print('1) List Courses')
            print('2) Add New Course')
            print('3) Update Course')
            print('4) Delete Course')
            print('5) List Students')
            print('6) Add New Student')
            print('7) Update Student')
            print('8) Delete Student')
            print('9) Assign Student to course')
            print('10) Print Course Students Codes')
            print('11) Print Student Courses')
            print('12) Back to Departments')
            try:
                choice = int(input('What do you want to do?'))
            except ValueError:
                print('please Enter A valid Choice')
            switcher = {
                1: self.print_department_courses,
                2: self.add_course,
                3: self.update_department_course,
                4: self.delete_department_course,
                5: self.print_department_students,
                6: self.add_student,
                7: self.update_department_student,
                8: self.delete_department_student,
                9: self.assign_course_to_student,
                10: self.print_course_students,
                11: self.print_student_courses
            }
            switcher.get(choice, CommnFunctions.invalid_choice)()
