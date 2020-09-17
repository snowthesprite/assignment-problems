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

print('Did the class Queue() make an empty list?')
assert q.data == [], 'No it did not make an empty list'
print('Yes it did')
print('')

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print('Is {} the right list that Queue()s enqueue() function made?'.format(q.data))
assert q.data == ['a', 'b', 'c'], 'No, enqueue() did not make the right list'
print('Yes enqueue() made the right list')
print('')

q.dequeue()

print('Is {} the right modification that dequeue() made to data?'.format(q.data))
assert q.data == ['b', 'c'], 'No dequeue() did not make the right modification'
print('Yes, dequeue() did make the right modification')
print('')

print('Is {} the right element for peek() to show?'.format(q.peek()))
assert q.peek() == 'b', 'No, peek() did not show the right element'
print('Yes, peek() showed the right element')
print('')

print('Did peek() take off an element of data when it showed us it?')
assert q.data == ['b', 'c'], 'Yes it did take off and element'
print('No it did not take off an element')
