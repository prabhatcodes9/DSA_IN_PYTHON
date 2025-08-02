# Search for an Element

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def search_element(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    
    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result
    
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.display())
print(ll.search_element(10))
        