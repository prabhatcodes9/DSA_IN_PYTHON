# Delete from beginning

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

    def delete_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -=1
        return popped_node


    
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
ll.delete_first()
print(ll.display())
        