class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def deleteDuplicates(self):
        validated = set()
        current = self.head
        prev = None

        while current:
            if current.value in validated:
                prev.next = current.next
            else:   
                validated.add(current.value) 
                prev = current        
            current = current.next

ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
print(ll)

ll.deleteDuplicates()
print(ll)


    