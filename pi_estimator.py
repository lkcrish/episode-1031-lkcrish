mport random

total_num - 10000
darts_in_circle = 0
for i in range(total_num):
    dartx = random.random()
    darty = random.random()
    if dartx*dartx + darty*darty <= 1:
        darts_in_circle += 1
    print(f'Our estimate for pi is {4.0* darts_in_circle /total_num})')

