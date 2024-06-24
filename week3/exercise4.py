class Queue:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.front = self.capacity = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity

    def is_full(self):
        return self.capacity >= self.max_capacity

    def is_empty(self):
        return self.capacity == 0

    def enqueue(self, item):
        if self.is_full():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.max_capacity)
        self.Q[self.rear] = item
        self.capacity += 1
        print(f"{item}: Enqueue success.")

    def dequeue(self):
        if self.is_empty():
            print("Empty")
            return
        print(f"{self.Q[self.front]}: dequeue from queue: ")
        self.front = (self.front + 1) % (self.max_capacity)
        self.capacity -= 1

    def take_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.Q[self.front]


queue1 = Queue(5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())

print(queue1.take_front())

print(queue1.dequeue())

print(queue1.take_front())

print(queue1.dequeue())

print(queue1.is_empty())
