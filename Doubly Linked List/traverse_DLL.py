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

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

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

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# reverse traversal of Doubly Linked List
    
    def reverse_traverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev

newDLL = DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
print(newDLL)
newDLL.prepend(50)
print(newDLL)
newDLL.traverse()
newDLL.reverse_traverse()

# Time Complexity is O(N)
# Space Complexity is O(1)



