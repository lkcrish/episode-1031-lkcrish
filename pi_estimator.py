mport random

total_num - 10000
darts_in_circle = 0
for i in range(total_num):
    dartx = random.random()
    darty = random.random()
    print(f'dart{i} is at ({dartx}, {darty})')

