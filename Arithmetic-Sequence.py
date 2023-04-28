# Arithmetic sequence
# Ex. 4, 7, 10, 13, 16, ... 

def sequence(start, step, number):
    sequence = []
    sum = start
    for number in range(1, number+1):
        sequence.append(sum)
        sum += step
    return sequence

start = int(input("Start:\n"))
step = int(input("Step:\n"))
number = int(input("Number:\n"))

print(sequence(start, step, number))