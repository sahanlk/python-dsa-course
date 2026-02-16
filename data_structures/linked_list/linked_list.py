"""
Implementation of a Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        """ Just a nice representation for the Node """
        return f"<Node: {self.value}>"


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        """
        Adding a node to the end

        Time Complexity: O(1)
        """
        new_node = Node(value)
        if not self.head:  # Edge case: If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        """
        Removing the last node (tail)

        Time Complexity: O(n)
        """
        if self.length == 0:  # Edge case: empty list
            return

        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        Add n item to the beginning

        Time Complexity: O(1)
        """
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop_first(self):
        """
        Remove the first node from the list.

        Time Complexity: O(1)
        """
        if self.length == 0:
            return

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """
        Get a node by index

        Time Complexity: O(n)
        """
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        """
        Update the value of a Node.

        Time Complexity: O(n)
        """
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Insert a node into a given index.

        Time Complexity: O(n)
        """
        if index > self.length or index < 0:
            return False
        elif index == self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)

        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Remove a node from the given index.
        """
        if index >= self.length or index < 0:
            return
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def dump(self):
        """ Visualizing the Linked List """
        node = self.head
        while node:
            print(f"{node} {'->' if node.next else '\n'} ", end="")
            node = node.next


if __name__ == "__main__":
    l = LinkedList(10)
    l.append(20)
    l.append(30)
    # l.append(40)
    # l.append(50)
    # l.append(98)
    # print(l.pop_first())
    l.insert(3, 87)
    l.insert(4, 60)
    l.remove(3)
    l.dump()
