class Node:
    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    def append(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first node with the given value."""
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        """Print the list."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.display()  # Output: 5 -> 10 -> 20 -> None
ll.delete(10)
ll.display()  # Output: 5 -> 20 -> None
