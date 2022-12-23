from Src.Collages.CollegeNode import CollegeNode


class Colleges:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_head(self, college_node: CollegeNode):
        self.head = college_node
        self.size += 1

    def add_new_college(self):
        new_college_data = CollegeNode.get_user_college_data()
        college_node = CollegeNode(new_college_data)
        college_node.set_next_node(self.head)
        self.add_to_head(college_node)
        self.print_list()

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.get_id() + ")" + temp.get_name())
            temp = temp.get_next_node()

    def search_by_name(self, name):
        temp = self.head
        while temp is not None:
            if temp.get_name() == name:
                return temp
            temp = temp.get_next_node()
        return False

    def search_by_id(self, collage_id):
        temp = self.head
        while temp is not None:
            if temp.get_id() == collage_id:
                return temp
            temp = temp.get_next_node()
        return False

    def update_college(self):
        name = input("Enter the college Name you want to update: ")
        college = self.search_by_name(name)
        if college:
            college.update_college()
        else:
            print("Invalid college Name Please try again")

    def delete_college(self):
        college_name = input("Enter the course Name you want to delete: ")
        deleted_college = self.search_by_name(college_name)
        if deleted_college:
            temp = self.head
            if temp.get_id() == deleted_college.get_id():
                self.head = temp.get_next_node()
                return True
            while temp.get_next_node() is not None:
                if temp.get_next_node().get_id() == deleted_college.get_id():
                    temp.set_next_node(deleted_college.get_next_node())
                    deleted_college.set_next_node(None)
                    return True
                temp = temp.get_next_node()
        else:
            print("invalid course")
        return False

    def is_empty(self):
        return self.size == 0

    def choice_collage(self):
        self.print_list()
        collage_id = input('Enter the Collage id ')
        collage = self.search_by_id(collage_id)
        if collage:
            collage.collage_options()
        else:
            print('Please Enter A Valid collage Id')



