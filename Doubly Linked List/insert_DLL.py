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

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1, index, -1):
                current = current.prev
        return current
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print('Index out of bounds')
            return
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp = self.get(index-1)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.length +=1

newDLL = DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
print(newDLL)
print(newDLL.insert(0, 20))
print(newDLL)

# Time Complexity is O(N)
# Space Complexity is O(1)