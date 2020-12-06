from tree import *

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

print('Does the get_children function work?')

assert get_children('e', edges) == ['g', 'i', 'a' ], 'Not for e'

assert get_children('c', edges) == [], 'Not for c'

assert get_children('f', edges) == ['h'], 'Not for f'

print('Yes, it does!')
print()

print('Does the get_parents function work?')

assert get_parents('e', edges) == [], 'Not for e'

assert get_parents('c', edges) == ['a'], 'Not for c'

assert get_parents('f', edges) == ['d'], 'Not for f'

print('Yes, it does!')
print()

print('Does the get_root function work?')

assert get_root(edges) == ['e'], 'No, it does not'

print('Yes it does!')