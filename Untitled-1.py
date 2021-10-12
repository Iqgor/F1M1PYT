def add(getal1, getal2):
    som = getal1+getal2
    print(som)

add(31, 56)
add(100, 43)

def multiply(getal3, getal4):
    som = getal3*getal4 
    print(som)

multiply(50,325)
import random
def roll_dice():
    rand_getal = random.randrange(1,7)
    return rand_getal

r1 = roll_dice()
r2 = roll_dice()
r3 = roll_dice()
r4 = roll_dice()
r5 = roll_dice()
r6 = roll_dice()

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)