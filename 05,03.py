numbers = input("Enter numbers split by space:").split(' ')
count = {}
for number in numbers:
    if count.get(number) is None:
        count[number] = 1
    else:
        count[number] += 1
    print(f" {key} - {value} times ")