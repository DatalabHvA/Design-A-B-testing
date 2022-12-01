import cv2
import sys
import glob
import os
import ctypes
import random
import numpy as np
from matplotlib import pyplot as plt
import argparse

p = argparse.ArgumentParser()
p.add_argument('-n', action = 'store', type = int, dest = 'n', default = 25)
p.add_argument('-folder', action = 'store', dest = 'folder', default = 'test1')
args = p.parse_args()

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname + '/designs/'+ getattr(args,'folder'))

image_list = []
filename_list = [] 

z = cv2.imread("./../z.png")
z = cv2.resize(z, (900, 900))

m = cv2.imread("./../m.png")
m = cv2.resize(m, (900, 900))

for filename in glob.glob("*.png"):
    img = cv2.imread(filename)
    imS = cv2.resize(img, (900, 900))
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
        cv2.moveWindow(winname, 60,30)  # Move it to (40,30)
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
            ctypes.windll.user32.MessageBoxW(0, "path does not exist", "Error", 1)
    cv2.destroyAllWindows()

D = {x:score.count(x) for x in set(score)}

plt.bar(*zip(*D.items()))
plt.show()