from collections import deque
my_deque = deque()
customer = ""
while customer != "END":
    customer = input("Enter customer name(or ‘END’ for the last people in the line): ")
    if customer == "END":
        break
    elif customer == "PAID":
        for person in my_deque:
            print(person)
        my_deque.clear()
    else:
        my_deque.append(customer)
print(f"Left people in the line : {len(my_deque)} people.")
