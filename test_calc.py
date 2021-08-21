from PIL import Image
import numpy as np

an_image = Image.open("Images/The_List_SS_1.png")

image_sequence = an_image.getdata()
image_array = np.array(image_sequence)

#At 14 zoom (from bottom) 141 pix = 2km so 1 pix = 14.1 m so 1 pix = 201.1 metres^2
#Assuming RGB formating

count = 0

for x in image_array:
    if((x[2] > x[0]+5) and (x[2] > x[1]+5)):
        count += 1


print("Square metres of water: ",count*201.1)
