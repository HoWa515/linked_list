# -------node
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

# ------linked list
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


    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True  # pass to function calls it

l=Linked_List(1)
l.append(2)
l.print_list()


