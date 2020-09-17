import matplotlib.pyplot as plt

def collatz_iterations(number) : 
    run_amount = 0
    while number != 1 : 
        if number % 2 == 0 : 
            number = number / 2
            run_amount += 1
        else : 
            number = (number * 3) + 1
            run_amount += 1
    return run_amount

def highest_collatz(max) :
    collatz_holder = []
    for number in range(1,max) :
        collatz_holder.append(collatz_iterations(number))
    max_collatz = 0
    for num in collatz_holder : 
        if num > max_collatz : 
            max_collatz = num
    return collatz_holder.index(max_collatz)

print('Is {} the correnct amount of Collatz iterations for 13?'.format(collatz_iterations(13)))
assert collatz_iterations(13) == 9, 'No its not'
print('Yes it is!')
print('')

print('{} is the number between 1 and 1000 that has the highest number of Collatz iterations'.format(highest_collatz(1000)))

#The chart is just showing up black and I have no idea what is going on it 
plt.style.use('bmh')
x_coords = [counting for counting in range(1,1000)]
y_coords = [collatz_iterations(number) for number in range(1,1000)]
plt.plot(x_coords, y_coords)
plt.xlabel('Number')
plt.ylabel('Collatz Number')
plt.title('Collatz Plot')
plt.savefig('plot.png')
