class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '->'
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def delete_all(self):
        if self.length == 0:
            return 
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

cslinkedlist = CSLinkedList()
cslinkedlist.prepend(50)
cslinkedlist.prepend(70)
cslinkedlist.prepend(30)
cslinkedlist.prepend(80)
cslinkedlist.prepend(10)
print(cslinkedlist)

print(cslinkedlist.delete_all())

# Time Complexity is O(1)
# Space Complexity is O(1)