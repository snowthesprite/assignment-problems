def even_odd_tuples(numbers) :
    return [(n,'even') if n % 2 == 0 else (n,'odd') for n in numbers]

def even_odd_dict(numbers) :
    #return {(n,'even') if n % 2 == 0 else (n,'odd') for n in numbers}
    return {n : ('even' if n % 2 == 0 else 'odd)'  for n in numbers }

#print(even_odd_tuples([1,2,3,5,8,11]))

print(even_odd_dict([1,2,3,5,8,11]))