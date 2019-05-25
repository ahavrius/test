# solution.py

## Task
The task is to develop a console tool which finds similar images in a given folder and prints similar pairs. We provide you with an example dataset for development. There are three types of similarity:
  - duplicate (images which are exactly the same)
  - modification (images which differ by size, blur level or noise filters)
  - similar (images of the same scene from another angle)

The images are marked in the example_dataset with words in the file names that correspond to the type of similarity. The minimal acceptable solution should be able to find “duplicates”. The complete solution should handle all three types of similarity.

### Example
Exampleof solution interface with the example dataset:

- python solution.py       
usage: solution.py [-h] --path PATH 
solution.py: error: the following arguments are required: --path

- python solution.py --help
usage: solution.py [-h] --path PATH

First test task on images similarity.

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           folder with images

- python solution.py --path ./dev_dataset 
4_similar.jpg 4.jpg
11_modification.jpg 11.jpg
11_modification.jpg 11_duplicate.jpg
6_similar.jpg 6.jpg
11.jpg 11_duplicate.jpg
15_modification.jpg 15.jpg
1.jpg 1_duplicate.jpg

### Solution

The simpliest implementation is to ignore shapss and to compare only the color gamuts. So I find the mean value of RBG variety and use euclidean distance to pair images. Empirically I choose 10 as a level of reliability.
