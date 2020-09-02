class Queue
    def __init__(self):
        self.data = []

    def enqueue(self,new_data):
        self.data.append(new_data)

    def dequeue(self):
        self.data.pop(0)

    def peek(self):
        return self.data[0]

