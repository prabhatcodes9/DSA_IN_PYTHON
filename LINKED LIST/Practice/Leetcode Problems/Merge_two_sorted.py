class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next 
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    

# Example Usage
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

print("List 1:")
list1.display()
print("List 2:")
list2.display()

# Merge the two sorted linked lists
merged_head = Solution(list1.head, list2.head)

print("\nMerged Sorted Linked List:")
temp = merged_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
