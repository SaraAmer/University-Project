from Src.Courses.Courses import Courses
from Src.Students.Students import Student
from Src.StudentCourses.SudentCourses import StudentCourses
from Src.Collages.College import Colleges
from Src.Helper import CommnFunctions

choice = 0
course = Courses()
students = Student()
collage = Colleges()


while choice != 6:
    print('1) Choose Collage')
    print('2) List Collages')
    print('3) Add Collage')
    print('4) Update Collage')
    print('5) delete Collage')
    print('6) Exit')
    try:
        choice = int(input('Enter Your Choice: '))
    except ValueError:
        CommnFunctions.invalid_choice()
    switcher = {
        1: collage.choice_collage,
        2: collage.print_list,
        3: collage.add_new_college,
        4: collage.update_college,
        5: collage.delete_college
    }
    switcher.get(choice, CommnFunctions.invalid_choice)()
