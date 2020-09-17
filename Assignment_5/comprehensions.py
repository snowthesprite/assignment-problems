def even_odd_tuples(numbers) :
    return [(n,'even') if n % 2 == 0 else (n,'odd') for n in numbers]

def even_odd_dict(numbers) :
    return {n : ('even' if n % 2 == 0 else 'odd') for n in numbers }

print('Did even_odd_tuples make the right list of tuples?')
assert even_odd_tuples([1,2,3,5,8,11]) == [(1,'odd'),(2,'even'),(3,'odd'),(5,'odd'),(8,'even'),(11,'odd')]
print('Yes, it did make the right list of tuples')
print('')

print('Did even_odd_dict make the right dictionary?')
assert even_odd_dict([1,2,3,5,8,11]) == {1:'odd', 2:'even', 3:'odd', 5:'odd', 8:'even', 11:'odd'}
print('Yes, it did make the right dictionary!')
print('')

#the dictionary and list are long so I'm not gonna put them in the print statements.