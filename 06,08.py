odd_set = set()
even_set = set()

n = int(input())
for i in range(1, n+1):
    name = input()
    value_name = sum(ord(char) for char in name) // i
    if value_name % 2 == 0:
        even_set.add(value_name)
    else:
        odd_set.add(value_name)
odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    result = odd_set.union(even_set)
    print(*result)
if odd_sum > even_sum:
    result_2 = odd_set.difference(even_set)
    print(*result_2)
if even_sum > odd_sum:
    result_3 = even_set.symmetric_difference(odd_set)
    print(*result_3)
