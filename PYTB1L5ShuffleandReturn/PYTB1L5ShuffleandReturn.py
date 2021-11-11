import random
def randome(woord1):
    randomised1 = ''.join(random.sample(woord1, len(woord1)))
    return randomised1 
print(randome("botje"))
print(randome("water"))
print(randome("huis"))
print(randome("kaas"))
print(randome("telefoon"))
print(randome("woontplaats"))
print("botje")
print("water")
print("huis")
print("telefoon")
print("huis")
print("woonplaats")
