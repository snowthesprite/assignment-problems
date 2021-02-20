from approximations_of_randomness import *
from linked_list2 import *

flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}

print('The list of who guessed the best goes, from best to worst : {}'.format(most_accurate(flips)))
print()
print('{} had the best guess of randomness.'.format(most_accurate(flips)[0]))
print()

linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')

print('Is the linked list the correct length?')
assert linked_list.length() == 4, 'No it is not'
print('Yes it is')
print()

print('Are the indexies correct for the nodes?')
assert linked_list.head.index == 0, 'Index 0 is not correct'

assert linked_list.head.next.index == 1, 'Index 1 is not correct'

assert linked_list.head.next.next.index == 2, 'Index 2 is not correct'

assert linked_list.head.next.next.next.index == 3, 'Index 3 is not correct'
print('Yes they are')
print()

print('Is get_node working correctly?')
assert linked_list.get_node(0).data == 'a', 'Not for node 0'

assert linked_list.get_node(1).data == 'b', 'Not for node 1'

assert linked_list.get_node(2).data == 'e', 'Not for node 2'

assert linked_list.get_node(3).data == 'f', 'Not for node 3'
print('Yes it is!')
