import studentNode


class studentNode:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node


class student:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_head(self, value):
        self.head = studentNode(value, self.head)
        self.size += 1

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            # assert isinstance(temp.next_node, Node)
            temp = temp.next_node

    def add_to_tail(self, value):
        temp = self.head
        if temp is None:
            self.head = studentNode(value)
            self.size += 1
            return
        while temp.next_node is not None:
            temp = temp.next_node
        temp.next_node = studentNode(value)
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def sorted_insert(self, value):
        temp = self.head
        if temp is None or temp.value > value:
            self.head = studentNode(value, temp)
            self.size += 1
            return
        while temp.next_node is not None and temp.next_node.value < value:
            temp = temp.next_node

        temp.next_node = studentNode(value, temp.next_node)
        self.size += 1