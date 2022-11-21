import numpy as np
from PIL import Image

filename = 'output/seven_weights.png'
input = open("output\\sevens_weights.txt")
weights = np.array(input.read()[1:-1].split(','))
weights_num = weights.astype(np.float)

image = Image.open(filename)
iter = 0

for i in range(28):
    for j in range(28):
        image.putpixel((i, j), (0, 0, 0))
        new_color = round(255 * weights_num[iter])
        image.putpixel((i, j), (new_color, new_color, new_color))
        iter += 1
image.show()
