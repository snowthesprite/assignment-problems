from count_compression import *
from linked_list import *

assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)]

assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)]

assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]) == 'aaabbcaaaa'
assert count_decompression([('2',2), ('3',1), ('4',5)]) == '22344444'

A = Node(4)

assert A.data == 4

assert A.next == None

B = Node(8)
A.next = B

assert A.next.data == 8

linked_list = LinkedList(4)

assert linked_list.head.data == 4

linked_list.append(8)

assert linked_list.head.next.data == 8

linked_list.append(9)

linked_list.print_data()
assert linked_list.length() == 3
