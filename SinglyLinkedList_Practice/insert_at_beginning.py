# Insert at the beginning

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result

ll = LinkedList()
ll.prepend(5)
ll.prepend(10)
print(ll.display())
        