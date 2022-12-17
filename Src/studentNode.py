
number_student = int(input("How many students You want to add: "))

student_list = []
for i in range(0, number_student):
    student_id=int(input("Enter id:"))
    student_name = input("enter name? ")
    student_gender = input("enter gender? ")
    student_college = input("enter college ")
    student_department =input("enter department ")
    student_number =int(input("Enter number:"))
    student_list.append([student_id,student_name, student_gender, student_college,student_department,student_number])





def __init__(self, value):
    self.value = value
    MyClass.update(value)


def search_by_id(self, student_id):
    temp = self.head
    while temp is not None:
        if temp.id == student_id:
            return temp
        temp = temp.next_node
    return False


def search_by_name(self, student_name):
    temp = self.head
    while temp is not None:
        if temp.name == student_name:
            return temp
        temp = temp.next_node
    return False1