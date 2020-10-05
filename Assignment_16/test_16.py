from count_compression import *
from linked_list import *

assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)]

assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)]