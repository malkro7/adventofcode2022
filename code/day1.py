from numpy import number


import pandas as pd
import numpy as np
with open("/home/sree/Documents/aoc/day1.txt") as fp:
    Lines = fp.readlines()
    count=0
    value=0
    final=0
    list=[]
    for line in Lines:
        if (line !='\n'):
            value += int(line)
        else:
            list.append(value)
            count += 1  
            value=0
    list=sorted(list)
    print(list[-1],":",list[-2],":",list[-3])
    print(list[-1]+list[-2]+list[-3])