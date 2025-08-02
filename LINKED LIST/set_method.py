class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append new value to the linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    # Print linked list
    def __str__(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return " -> ".join(values)

    # Get node at a specific index
    def get(self, index):
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current  # Return Node, not current.value
            current = current.next
            count += 1
        return None

    # Set value at a specific index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

# Example usage:
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

print(new_linked_list)  # 10 -> 20 -> 30
print(new_linked_list.set_value(2, 50))  # True
print(new_linked_list)  # 10 -> 20 -> 50