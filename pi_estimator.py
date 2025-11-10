
import random
import sys

total_num = int(sys.argv[1])
darts_in_circle = 0
for i in range(total_num):
   print("Throwing dart...") 
   dartx = random.random()
    darty = random.random()
    print (f'dart {i} is at ({dartx}, {darty})')
    if dartx*dartx + darty*darty <= 1:
        darts_in_circle += 1
    print(f'Our estimate for pi is {4.0* darts_in_circle /total_num})')

