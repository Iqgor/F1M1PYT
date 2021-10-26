import time
from PIL import Image 
image = Image.open('C:\\Users\\herre\\Pictures\\moi.jpg') 
countdown = 1000
while countdown:
    print(countdown)
    time.sleep(0.005)
    countdown -= 1 
print("klaar")
image.show()

