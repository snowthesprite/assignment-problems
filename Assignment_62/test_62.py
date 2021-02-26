from bisection_search import *

print('Does bisection_search work?')

assert bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9, 'No'

print('Yes it does', "\n")

print('Suppose you have a sorted list of 16 elements. What is the greatest number of iterations of bisection search that would be needed to find the index of any particular element in the list?', "\n")
print('Maximum should be 4 times. If you take the top index (15) and devide it by two (rounding if you get a fraction), you can only devide 4 times. Thus that is the maximum times the graph can be split until only one thing is left.', "\n")