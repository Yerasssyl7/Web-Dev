n = int(input())

i = 2
import math
while i <= n:
    if math.sqrt(i) % 1 == 0:
        print(i)
    i += 1