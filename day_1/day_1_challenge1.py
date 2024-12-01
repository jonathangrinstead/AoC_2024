with open('input.txt') as file:
    left_col = []
    right_col = []
    for line in file:
        all_nums = line.split()
        for i in range(0, len(all_nums)):
            if i % 2:
                left_col.append(all_nums[i])
            else:
                right_col.append(all_nums[i])

sorted_left = sorted(left_col)
sorted_right = sorted(right_col)

total_diff = 0

for a,b in zip(sorted_left, sorted_right):
    int_a = int(a)
    int_b = int(b)
    if a > b:
        total_diff += int_a - int_b
    else:
        total_diff += int_b - int_a

print(total_diff)

# Part 2

similarity_score = 0

for num in sorted_left:
    count = sorted_right.count(num)
    similarity_score += int(num) * count

print(similarity_score)
