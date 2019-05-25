from PIL import Image
import numpy as np
import glob
import sys
import os

def help():
    print("usage: solution.py [-h] --path PATH\n\n",
    "First test task on images similarity.\n\n",
    "optional arguments:\n",
    "  -h, --help            show this help message and exit\n",
    "  --path PATH           folder with images\n")
    sys.exit()

def error(str):
    print("usage: solution.py [-h] --path PATH\n",
    "solution.py: error: ", str, "\n")
    sys.exit()

if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
    help()
if len(sys.argv) == 1 or sys.argv[1] != "--path":
    error("the following arguments are required: --path")
if len(sys.argv) == 2:
    error("the following arguments are required: PATH")
if len(sys.argv) > 3:
    error("too many arguments")

if not os.path.isdir(sys.argv[2]):
    error("folder is not found")

path = sys.argv[2] + "/*.jpg"
image_list = [Image.open(filename) for filename in glob.glob(path)]
np_image_list = [np.array(img) for img in image_list]

rgb_list = [np.sum(np.sum(np_img[ : , : ], axis = 0), axis = 0) // (np_img.shape[0] * np_img.shape[1])
            for np_img in np_image_list]

delta = np.array ([[ np.sqrt(sum((img1 - img2)**2))
                    for img1 in rgb_list] for img2 in rgb_list],
                    dtype = np.uint16)

path_shift = len(sys.argv[2]) + 1
level = 10
for i in range(len(rgb_list)):
    for j in range(i, len(rgb_list)):
        if i != j and delta[i, j] < level:
            print(image_list[i].filename[path_shift : ],
                  image_list[j].filename[path_shift : ])