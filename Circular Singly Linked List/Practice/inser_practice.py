# 1. Implement a circular linked list with insert at beginning, insert at end, and display functions.

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
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1


    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception('Index out of range')
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                self.tail.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head
            for _ in range (index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
                
        self.length +=1

    def count(self, index):
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            current = current.next
            count +=1 
        return count
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def delete_index(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        prev_node = self.get_element(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -=1
        return popped_node
    
    def split_list(self):
        if self.head is None or self.head.next == self.head:
            return None, None
        
        slow = self.head
        fast = self.head

        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        head1 = self.head
        head2 = slow.next

        slow.next = head1
        if fast.next == self.head:
            fast.next = head2
        else:
            fast.next.next = head2

        return head1, head2


cslinkedlist = CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(40)
print(cslinkedlist)
cslinkedlist.insert(2, 30)
print(cslinkedlist)
cslinkedlist.prepend(100)
print(cslinkedlist)
print(cslinkedlist.count)
head1, head2 = cslinkedlist.split_list()


        
