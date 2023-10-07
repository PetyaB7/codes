user_points=0
red=0
orange=0
yellow=0
white=0
black=0
other=0
rounds=int(input("How many rounds you want: "))
for rounds in range(0,rounds):
    gusses=input()
if gusses =='red':
    user_points+=5
    red+=1
elif gusses=='orange':
    user_points+=10
    orange+=1
elif gusses=='yellow':
    user_points+=15
    yellow+=1
elif gusses=='white':
    user_points+=20
    white+=1
elif gusses=='black':
    user_points//2
    black+=1
else:
    other+=1
print(f"total points:{user_points}")
print(f"Red sector:{red}")
print(f"Orange sector:{orange}")
print(f"Yellow sector:{yellow}")
print(f"White sector:{white}")
print(f"Black sector:{black}")
print(f"Other sector:{other}")