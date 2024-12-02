input_array = []
with open('input.txt') as file:
    for line in file:
        input_array.append(line.strip().split(' '))

safe_count = 0

for array in input_array:
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            break
        else:
            safe_count += 1

print(safe_count)
