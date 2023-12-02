n = int(input())
matrix = []

for y in range(n):
    numbers = input().split(", ")
    row = []
    for num in numbers:
        row.append(int(num))
    matrix.append(row)

sum_d = 0
for i in range(n):
    for j in range(i+1):
        sum_d += matrix[i][j]
print(sum_d)
