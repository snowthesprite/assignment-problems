from doubly_linked_list import *

doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
print(doubly_linked_list.head.next.next.prev.data)
doubly_linked_list.delete(3)

current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]
for _ in range(3):
    current_node = current_node.prev
    node_values.append(current_node.data)

assert node_values ==['e', 'c', 'b', 'a']
