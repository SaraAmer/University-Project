from Src.Courses import Courses
from Src.Students import Students


class StudentCourses:
    def __init__(self, data):
        self.__course_code = data['course_code']
        self.__student_id = data['student_id']
        self.__grade = data['grade']
        self.__next_student = None
        self.__next_course = None

    def get_course_code(self):
        return self.__course_code

    def set_course_code(self, course_code):
        self.__course_code = course_code

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_next_student(self, next_student):
        self.__next_student = next_student

    def get_next_student(self):
        return self.__next_student

    def set_next_course(self, next_course):
        self.__next_course = next_course

    def get_next_course(self):
        return self.__next_course

    @staticmethod
    def get_course_student_data():
        course_student_data = {
            'course_code': input("Enter the Course code: "),
            'student_id': input("Enter the Student id: "),
            'grade': input("Enter the Student Grade: ")
        }
        return course_student_data
    
    #@todo multi level of identition is not a clean code please refactor this to functions
    @staticmethod
    def assign_student_to_course(course_list, student_list):
        entered_data = StudentCourses.get_course_student_data()
        student_course = StudentCourses(entered_data)
        course_code = student_course.get_course_code()
        student_id = student_course.get_student_id()
        course = Courses.Courses.search_by_code(course_code, course_list)
        student = Students.Student.search_by_id(student_id, student_list)
        if course and student:
            course_last_student = course.get_course_last_student()
            student_last_course = student.get_student_last_course()
            if course_last_student is None:
                course.set_students(student_course)
            else:
                course_last_student.set_next_student(student_course)
            if student_last_course is None:
                student.set_courses(student_course)
            else:
                student_last_course.set_next_course(student_course)
        else:
            print('Please Enter a valid student id and course code')


        

