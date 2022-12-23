from Src.Courses.Courses import Courses
from Src.Students.Students import Student
from Src.StudentCourses.SudentCourses import StudentCourses
from Src.Collages.College import Colleges

choice = 1
course = Courses()
students = Student()
collage = Colleges()


def invalid_choice():
    print('please Enter a valid Choice')


while choice != 0:
    print('1) Choose Collage')
    print('2) List Collages')
    print('3) Add Collage')
    print('4) Update Collage')
    print('5) delete Collage')
    try:
        choice = int(input('Enter Your Choice: '))
    except ValueError:
        invalid_choice()
    switcher = {
        1: collage.choice_collage,
        2: collage.print_list,
        3: collage.add_new_college,
        4: collage.update_college,
        5: collage.delete_college
    }
    switcher.get(choice, invalid_choice)()
