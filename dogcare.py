food = int(input("How much kilograms you buy: "))
eatfood = int(input("How much grams dog eat: "))

while food != 'Stop':
    money = food*5.50
    leftovers = food-eatfood
    morefood = eatfood-food

if food < eatfood:
    print(f"Food is not enough. You need {morefood} grams more. So you spent {money} leva for food.")
if food == eatfood:
    print(f"Food is enough. Leftovers:0 grams. So you spent {money} leva for food.")
if food > eatfood:
    print(f"Food is enough. Leftovers:{leftovers} grams. So you spent {money} leva for food.")
    