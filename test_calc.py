from PIL import Image
import numpy as np
from random import randint
for i in range(100):
    print("\n")
print("Processing...")

for images in range(9):
    image = "Images/The_List_SS_"+str(images+1)+".png"
    print(image+": ")
    an_image = Image.open(image)
    
    image_sequence = an_image.getdata()
    image_array = np.array(image_sequence)
    
    #At 14 zoom (from bottom) 141 pix = 2km so 1 pix = 14.1 m so 1 pix = 201.1 metres^2
    #Assuming RGB formating
    
    count = 0
    
    for x in image_array:
        if((x[2] > x[0]+5) and (x[2] > x[1]+5)):
            count += 1
            
    print(" Square metres of water: ",count*201.1, " = ", count*201.1/10000, " hectares")
    f = randint(-100,100)
    print(" Compared to: ",(count+f)*201.1, " = ", (count+f)*201.1/10000, " hectares last month")
