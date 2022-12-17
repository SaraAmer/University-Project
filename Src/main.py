import Courses
choice = 167
while choice != 0:
    print('1) List Courses')
    print('2) Add New Course')
    print('3) Update Course')
    print('4) Delete Course')
    choice = int(input('What do you want to do?'))
    print(choice, 'choice')
    course = Courses.Courses()
    switcher = {
        1: course.print_list,
        2: course.add_new_course,
        3: course.update_course
    }
    switcher[choice]()
