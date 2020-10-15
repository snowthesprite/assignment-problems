from linked_list3 import *

linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
assert linked_list.length() == 5
linked_list.print_data()
print()

assert linked_list.get_node(2).data == 'c'
linked_list.delete(2)

assert linked_list.length() == 4
assert linked_list.get_node(2).data == 'd'
linked_list.print_data()
print()

linked_list.insert('f', 2)
assert linked_list.length() == 5
assert linked_list.get_node(2).data == 'f'
linked_list.print_data()