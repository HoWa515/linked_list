# node
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

my_list=Linked_List(5)
print(my_list.head.value)
print(my_list.tail.value)