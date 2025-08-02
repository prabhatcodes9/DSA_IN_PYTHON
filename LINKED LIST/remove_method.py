class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Add a node at the end
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1

    # Print the list
    def __str__(self):
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " -> ".join(values) if values else "Empty List"

    # Get node at index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None

    # Set value at index
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    # Insert at specific index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.length += 1
        return True

    # Remove node at index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            popped_node = self.head
            self.head = self.head.next
        else:
            prev_node = self.get(index - 1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node


# Example usage:
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

print(new_linked_list)  # 10 -> 20 -> 30

new_linked_list.set_value(2, 50)
print(new_linked_list)  # 10 -> 20 -> 50

new_linked_list.insert(1, 15)
print(new_linked_list)  # 10 -> 15 -> 20 -> 50

removed = new_linked_list.remove(2)
print(f"Removed: {removed.value}")  # Removed: 20
print(new_linked_list)  # 10 -> 15 -> 50