class Stack:
    def __init__(self):
        self.data = []

    def push(self,new_data):
        self.data.append(new_data)

    def pop(self):
        self.data.pop(len(data)-1)

    def peek(self):
        

s = Stack()

assert s.data == []

s.push('a')
s.push('b')
s.push('c')
print(s.data)
