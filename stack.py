class Stack:
    def __init__(self):
        self.data = []

    def push(self,new_data):
        self.data.append(new_data)

    def pop(self):
        self.data.pop(len(self.data)-1)

    def peek(self):
        return self.data[-1]
        

s = Stack()
print(s.data)

assert s.data == []

s.push('a')
s.push('b')
s.push('c')
print(s.data)
s.pop()
print(s.data)

print(s.peek())
print(s.data)
