import Courses
import Students
import Department
import College
choice = 1
course = Courses.Courses()
students = Students.Student()
Department = Department.Department()
College = College.Colleges()

while choice != 0:
    print('1) List Courses')
    print('2) Add New Course')
    print('3) Update Course')
    print('4) Delete Course')
    print('5) List Students')
    print('6) Add New Student')
    print('7) Update Student')
    print('8) Delete Student')
    choice = int(input('What do you want to do?'))
    print(choice, 'choice')
    switcher = {
        1: course.print_list,
        2: course.add_new_course,
        3: course.update_course,
        4: course.delete_course,
        5: students.print_list,
        6: students.add_new_student,
        7: students.update_student,
        8: students.delete_student
    }
    switcher.get(choice, 'invalid')()
