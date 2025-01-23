import sys
import random
num = random.randint(0, 1)
if num!= 0:
    print("{}".format(num))
    sys.exit(1)
print("{}".format(num))
sys.exit(0)