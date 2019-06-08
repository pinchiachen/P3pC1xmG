from importlib import reload
import time
import random

for i in range(0, 10):
    if i == 0:
        import Q2module
        print(Q2module.attr_X)
        time.sleep(random.uniform(0, 10))
    else:
        reload(Q2module)
        print(Q2module.attr_X)
        time.sleep(random.uniform(0, 10))

