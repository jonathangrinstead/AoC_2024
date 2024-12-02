input_array = []
with open('input.txt') as file:
    for line in file:
        input_array.append(line.strip().split(' '))

def is_safe_sequence(levels):
    if len(levels) < 2:
        return True
    levels = [int(x) for x in levels]
    is_increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels)-1))
    is_decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels)-1))
    return is_increasing or is_decreasing
count = 0
for sequence in input_array:
    if is_safe_sequence(sequence):
        count += 1

print(f"Number of safe sequences: {count}")


#challenge 2 

def is_safe_with_problem_dampener(levels):
    if is_safe_sequence(levels):
        return True
    if len(levels) < 2:
        return True
    levels = [int(x) for x in levels]
    for i in range(len(levels)):
        temp_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(temp_levels):
            return True
    return False

count = 0  
for sequence in input_array:
    if is_safe_with_problem_dampener(sequence):
        count += 1

print(f"Number of safe sequences with Problem Dampener: {count}")