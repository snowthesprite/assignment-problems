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

print('Did the class Stack() make an empty list?')
assert s.data == [], 'No it did not make an empty list'
print('Yes it did')
print('')

s.push('a')
s.push('b')
s.push('c')

print('Is {} the right list that Stack()s push() function made?'.format(s.data))
assert s.data == ['a', 'b', 'c'], 'No, push() did not make the right list'
print('Yes push() made the right list')
print('')

s.pop()

print('Is {} the right modification that pop() made to data?'.format(s.data))
assert s.data == ['a', 'b'], 'No pop() did not make the right modification'
print('Yes, pop() did make the right modification')
print('')

print('Is {} the right element for peek() to show?'.format(s.peek()))
assert s.peek() == 'b', 'No, peek() did not show the right element'
print('Yes, peek() showed the right element')
print('')

print('Did peek() take off an element of data when it showed us it?')
assert s.data == ['a', 'b'], 'Yes it did take off and element'
print('No it did not take off an element')
