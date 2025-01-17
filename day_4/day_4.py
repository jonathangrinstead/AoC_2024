count = 0

with open('input.txt') as file:
    rows = {}
    for line in file:
        count += line.count('XMAS') 
        count += line.count('XMAS'[::-1])
        for i in range(0, len(line)):
            if i in rows:
                rows[i] += line[i]
            else:
                rows[i] = line[i]

xmas_list = list('XMAS')

for key, value in rows.items():
   count += value.count('XMAS')
   count += value.count('XMAS'[::-1])
   
grid = []
max_key = max(rows.keys())
for i in range(max_key + 1):
    if i in rows:  
        grid.append(list(rows[i]))  

# Check diagonals
for i in range(len(grid) - 3):
    for j in range(len(grid[0]) - 3):  
        try:
            diagonal = ''.join(grid[i+k][j+k] for k in range(4))
            count += diagonal.count('XMAS')
            count += diagonal.count('XMAS'[::-1])
        except IndexError:
            continue
        
    for j in range(3, len(grid[0])):  
        try:
            diagonal = ''.join(grid[i+k][j-k] for k in range(4))
            count += diagonal.count('XMAS')
            count += diagonal.count('XMAS'[::-1])
        except IndexError:
            continue

print(count)

#Challenge 2