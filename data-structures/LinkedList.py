
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._count = 0

    def print_list(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

    @property
    def count(self):
        node = self.head
        while(node):
            self._count += 1
            node = node.next
        return self._count

    def insert_front(self, data):
        temp = self.head
        node = Node(data)
        self.head = node
        node.next = temp

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print('Node must be in the linked list')
            return
        new_node = Node(data)
        temp = prev_node.next
        prev_node.next = new_node
        new_node.next = temp

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def delete(self, position):
        if self.head == None:
            return 
        temp = self.head
        if position == 0:
            self.head = temp.next
            value = temp.data
            temp = None
            self._count -= 1
            return value

        for i in range(position-1):
            temp = temp.next 
            if temp is None:
                break

        if (temp.next is None) or (temp is None):
            return 

        next_pointer = temp.next.next
        value = temp.next.data
        temp.next = None
        temp.next = next_pointer
        self._count -= 1
        return value

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current 
            current = next
        self.head = previous

    def pop_without_deleting(self):
        return self.head.data

    def is_empty(self):
        return self.head is None

    def clear(self):
        for i in range(self.count):
            self.delete(0)
        return "emptied"







if __name__ == '__main__':
    linked_list = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    linked_list.head = node1
    linked_list.head.next = node2
    node2.next = node3
    linked_list.insert_front(0) #adding a new value to the front of the list (insert)
    linked_list.insert_after(node2, 5) #adding a new value after tne second node
    linked_list.insert_last(20) #adding a new value at the end of the list (push)
    linked_list.print_list() #printing the list

    