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

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next



my_list=Linked_List(5)
print(my_list.head.value)
print(my_list.tail.next)