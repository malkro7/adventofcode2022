import pandas as pd
import numpy as np
match=0
nomatch=0
overlap=0

def boundaryCheck(lb1,ub1,lb2,ub2):
    # global match
    # if (lb1>=lb2) and (ub2>=ub1):
    #     print(lb1,ub1,lb2,ub2,"included")
    #     match+=1
    # elif (lb2>=lb1) and (ub1>=ub2):
    #     print(lb1,ub1,lb2,ub2,"included")
    #     match+=1
    # else:
    #     print(lb1,ub1,lb2,ub2,"NOT included")
    global match
    global nomatch
    if(ub1>=lb2) and (ub2>=lb1):
        print(lb1,ub1,lb2,ub2,"overlap")
        match+=1
    else:
        print(lb1,ub1,lb2,ub2,"no overlap")
        nomatch+=1

with open("/home/sree/Documents/aoc/day4.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        l=line[:-1].split(",")
        l1=l[0].split("-")
        l2=l[1].split("-")
        boundaryCheck(int(l1[0]),int(l1[1],),int(l2[0]),int(l2[1]))
print(match)
print(nomatch)


        
