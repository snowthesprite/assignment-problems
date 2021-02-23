from hash_class import *

ht = HashTable(num_buckets = 3)
assert ht.buckets == [[], [], []]


assert ht.hash_function('cabbage') == 2 #(because 2+0+1+1+0+6+4 mod 3 = 14 mod 3 = 2)

ht.insert('cabbage', 5)

assert ht.buckets
[[], [], [('cabbage',5)]]

ht.insert('cab', 20)

assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]

ht.insert('c', 17)

assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

ht.insert('ac', 21)

assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]

assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21
