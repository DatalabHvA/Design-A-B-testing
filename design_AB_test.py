import cv2
import sys
import glob
import os
import ctypes
import random
import numpy as np
from matplotlib import pyplot as plt
import argparse
import time

p = argparse.ArgumentParser()
p.add_argument('-n', action = 'store', type = int, dest = 'n', default = 25)
p.add_argument('-folder', action = 'store', dest = 'folder', default = 'test1')
p.add_argument('-s', action = 'store', type = float, dest = 's', default = 1)
args = p.parse_args()

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname + '/designs/'+ getattr(args,'folder'))

image_list = []
filename_list = [] 

img_size = int(np.floor(900/getattr(args,'s')))

z = cv2.imread(dname+"/img/z.png")
z = cv2.resize(z, (img_size, img_size))

m = cv2.imread(dname+"/img/m.png")
m = cv2.resize(m, (img_size, img_size))

dot = cv2.imread(dname+"/img/dot.png")
dot = cv2.resize(dot, (2*img_size, img_size))

for filename in glob.glob("*.png"):
    img = cv2.imread(filename)
    imS = cv2.resize(img, (img_size, img_size))
    image_list.append(imS)
    filename_list.append(filename)

score = []

for i in range(getattr(args,'n')):
    letter = random.randrange(0, 2)
    position = random.randrange(0, 2)
    image_z = cv2.subtract(image_list[letter],cv2.bitwise_not(z))
    image_m = cv2.subtract(image_list[1-letter],cv2.bitwise_not(m))
    image_list2 = [image_z,image_m]
    image = np.concatenate((image_list2[position], image_list2[1-position]), axis=1)
    written = False
    while written == False:
        winname = "window"
        cv2.namedWindow(winname)        # Create a named window
        cv2.moveWindow(winname, 60,30)  # Move it to (60,30)
        cv2.imshow(winname, dot)
        cv2.waitKey(1000)
        cv2.imshow(winname, image)
        key = cv2.waitKey(0)
        char_key = chr(key%256)
        if (char_key == 'z'):
            score.append(os.path.splitext(filename_list[letter])[0])
            written = True
        elif (char_key == 'm'):
            score.append(os.path.splitext(filename_list[1-letter])[0])
            written = True
        else:
            ctypes.windll.user32.MessageBoxW(0, "kies één van de getoonde letters", "Error", 1)
    cv2.destroyAllWindows()

D = {x:score.count(x) for x in set(score)}

plt.bar(*zip(*D.items()))
plt.show()