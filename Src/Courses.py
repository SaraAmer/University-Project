import CoursesNode


class Courses:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_head(self,  course_node: CoursesNode):
        self.head = course_node
        self.size += 1

    def add_new_course(self):
        new_course_data = CoursesNode.CourseNode.get_user_course_data()
        course_node = CoursesNode.CourseNode(new_course_data)
        course_node.set_next_node(self.head)
        self.add_to_head(course_node)
        self.print_list()

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def print_list(self):
        temp = self.head
        print(temp)
        while temp is not None:
            print(temp.get_name())
            # assert isinstance(temp.next_node, Node)
            temp = temp.get_next_node()

    def search_by_name(self, name):
        temp = self.head
        while temp is not None:
            if temp.name == name:
                return temp
            temp = temp.get_next_node()
        return False

    def search_by_code(self, code):
        temp = self.head
        while temp is not None:
            if temp.code == code:
                return temp
            temp = temp.get_next_node()
        return False

    def update_course(self):
        name = input("Enter the Course Name")
        course = self.search_by_name(name)
        if course:
            course.update_course()
        else:
            print("Invalid Course Name Please try again")

    def delete_course(self, course_node: CoursesNode):
        temp = self.head
        if temp.code == course_node.code:
            self.head = temp.next_node
            return True

        while temp.next_node is not None:
            if temp.next_node.code == course_node.code:
                temp.next_node = course_node.next_node
                course_node.next_node = None
                return True
            temp = temp.next_node
        return False

    def is_empty(self):
        return self.size == 0






#
# courseName = input("Enter the course Name you want to update")
#
# updatedCourse = Course.search_by_name(courseName)
# if updatedCourse:
#     updatedCourse.name = input("Enter the new Name you want to update")
# else:
#     print('Invalid Course')
# Course.print_list()
# courseName = input("Enter the course Name you want to delete")
# deletedCourse = Course.search_by_name(courseName)
# if deletedCourse:
#     Course.delete_course(deletedCourse)
# else:
#     print('Invalid Course')
# Course.print_list()
