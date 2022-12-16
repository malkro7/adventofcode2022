import pandas as pd
import numpy as np
from collections import Counter
import re

# dupListL=[]
# dupListU=[]
# count=0

# def getDuplicate(s):
#     tempList=[]
#     l=int(len(s)/2)
#     s1=s[0:l]
#     s2=s[l:]

#     for x in s1:
#         for y in s2:
#             if (x==y):
#                 tempList.append(y)

#     #drop duplicates
#     tempList= [*set(tempList)]
#     for z in tempList:
#         if (ord(z) >= 97):
#            dupListL.append(z)
#         else:
#            dupListU.append(z)
        

# sumL=0
# sumU=0
count=0
tcount=0
grp=""
no_vals=0
listL=[]
listU=[]
def getBadges(l):
    collection = Counter(l)
    for key, val in collection.items():
        if (val == 3):
            global no_vals 
            no_vals+= 1
            if (ord(key) >=97):
                listL.append(key)
            else:
                listU.append(key)

s3=""
with open("/home/sree/Documents/aoc/day3.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        x=re.findall('[a-zA-Z]', line)
        x=[*set(x)]
        s=" ".join(x)
        s3=s3+" " + s
        count += 1
        if (count == 3):
            getBadges(s3)
            s3=""
            count=0
print(no_vals)
print(listL)
print(listU)
sumL=0
sumU=0
for x in listL:
    sumL+=(ord(x)-96)
print(sum)
for y in listU:
    sumU+=(ord(y)-38)
print(sumL, sumU, sumL+sumU)
# print (count)
# for l in dupListL:
#     sumL=sumL+(ord(l)-96)
# for u in dupListU:
#     sumU=sumU+(ord(u)-38)
# print(sumU,sumL, sumU+sumL)