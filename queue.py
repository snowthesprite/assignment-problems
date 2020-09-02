class Queue :
    def __init__(self):
        self.data = []

    def enqueue(self,new_data):
        self.data.append(new_data)

    def dequeue(self):
        self.data.pop(0)

    def peek(self):
        return self.data[0]

q = Queue()
print(q.data)

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q.data)

q.dequeue()
print(q.data)

print(q.peek())
print(q.data)