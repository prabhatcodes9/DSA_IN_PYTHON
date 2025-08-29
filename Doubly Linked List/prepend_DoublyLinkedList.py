class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result +=str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1

newDLL = DoublyLinkedList()
newDLL.prepend(10)
print(newDLL)
newDLL.prepend(20)
print(newDLL)
newDLL.prepend(30)
print(newDLL)
newDLL.prepend(40)
print(newDLL)

# Time Complexity is O(1)
# Space Complexity is O(1)