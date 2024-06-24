class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.head = Node("head")
        self.capacity = 0

    def is_empty(self):
        return self.capacity == 0

    def is_full(self):
        return self.capacity == self.max_capacity

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.capacity += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = remove.next
        self.capacity -= 1
        return remove.value

    def top(self):
        return self.head


stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
