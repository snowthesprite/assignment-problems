from count_compression import *
from linked_list import *

print('Does count_compression work for the given tests?')

assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)], 'count_compression does not work for "aaabbcaaaa"'

assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)], 'count_compression does not work for "22344444"'

print('Yes it does!')
print()

print('Does count_decompression work for the given tests?')

assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]) == 'aaabbcaaaa', "count_decompression does not work for [('a',3), ('b',2), ('c',1), ('a',4)]"

assert count_decompression([('2',2), ('3',1), ('4',5)]) == '22344444', "count_decompression does not work for [('2',2), ('3',1), ('4',5)]"

print('Yes it does!')
print() 

A = Node(4)

print('Did Node correctly make a node?')

assert A.data == 4, 'No it did not'

assert A.next == None, 'No it did not'

print('Yes it did!')
print()

B = Node(8)
A.next = B

print('Did A.next get properly set to the next node?')

assert A.next.data == 8, 'No it did not'

print('Yes it did!')
print()

linked_list = LinkedList(4)

assert linked_list.head.data == 4, 'No it did not'

linked_list.append(8)

assert linked_list.head.next.data == 8, 'No it did not'

linked_list.append(9)

linked_list.print_data()

assert linked_list.length() == 3, 'No it did not'
