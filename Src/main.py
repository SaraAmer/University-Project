from Src.Courses.Courses import Courses
from Src.Students.Students import Student
from Src.StudentCourses.SudentCourses import StudentCourses

choice = 1
course = Courses()
students = Student()
while choice != 0:
    print('1) List Courses')
    print('2) Add New Course')
    print('3) Update Course')
    print('4) Delete Course')
    print('5) List Students')
    print('6) Add New Student')
    print('7) Update Student')
    print('8) Delete Student')
    print('9) Assign Student to course')
    print('10) Print Course Students')
    print('11) Print Student Courses')
    choice = int(input('What do you want to do? '))
    print(choice, 'choice')
    switcher = {
        1: course.print_list,
        2: course.add_new_course,
        3: course.update_course,
        4: course.delete_course,
        5: Student.print_list,
        6: students.add_new_student,
        7: students.update_student,
        8: students.delete_student,
        9: StudentCourses.assign_student_to_course,
        10: Courses.print_course_students,
        11: Student.print_student_courses
    }
    switcher.get(choice, 'invalid')()
