import time 
from os  import system, name
def carmarker():
    system("cls")  
    print("Factory: ",str(factory))
    print("distruberter: ", str(distruberter))
    print("shop: ", str(shop))
    time.sleep(2)  
factory = ["car","car1"] 
distruberter = [] 
shop = []  
carmarker()
factory.remove("car1")
distruberter.insert(0, "car1")
carmarker()
distruberter.remove("car1")
shop.insert(0, "car1")
carmarker()
shop.remove("car1")
carmarker()
factory.remove("car")
distruberter.insert(0, "car")
carmarker()
distruberter.remove("car")
shop.insert(0, "car")
carmarker()
shop.remove("car")
carmarker()