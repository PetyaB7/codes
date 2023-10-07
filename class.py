import random

clas=['22101','22102','22103','22104','22105','22106','22107','22108','22109','22110','22111','22112','22113','22114','22115','22116','22117','22118','22119','22120','22121','22122','22123','22124','22125','22126','22127','22128','22129']
already_s=[]
s_students=[(x) for x in input("Who is ill: ").split(",")]
for s_student in s_students:
    clas.remove(s_student)

while True:
    p=random.choice(clas)
    if p in already_s:
        continue
    already_s.append(p)
    clas.remove(p)
    print(p)