# import math
# print(dir(math))

import random

a=random.randint(1,3)
print(a)

b=random.randrange(1,3)  #in randrange 3 will not included
print(b)

c=random.random()
print(c)

l=[4,5,3,4,6,7,65,4,12]
d=random.choice(l)
print(d)

f=[4,5,3,4,6,7,65,4,12]
e=random.shuffle(f)
print(e)