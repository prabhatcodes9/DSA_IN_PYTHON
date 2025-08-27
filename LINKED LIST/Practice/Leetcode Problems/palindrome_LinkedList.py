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
    
    def isPalindrome(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values == values[::-1]
    
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)


print(ll.isPalindrome())