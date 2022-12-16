import pandas as pd
import numpy as np
crates=[]
def buildCrates():
    global crates
    l1=['T','V','J','W','N','R','M','S']
    l2=['V','C','P','Q','J','D','W','B']
    l3=['P','R','D','H','F','J','B']
    l4=['D','N','M','B','P','R','F']
    l5=['B','T','P','R','V','H']
    l6=['T','P','B','C']
    l7=['L','P','R','J','B']
    l8=['W','B','Z','T','L','S','C','N']
    l9=['G','S','L']
    crates.append(l1[::-1])
    crates.append(l2[::-1])
    crates.append(l3[::-1])
    crates.append(l4[::-1])
    crates.append(l5[::-1])
    crates.append(l6[::-1])
    crates.append(l7[::-1])
    crates.append(l8[::-1])
    crates.append(l9[::-1])
  
def moveCrates(qty,frm,to):
    print(qty,frm,to)
    crates[to-1] = crates[to-1] + crates[frm-1][-qty:]
    for _ in range(qty):
        crates[(frm-1)].pop()
        

buildCrates()
with open("C:\Advent\data\day5.txt") as f:
    lines = f.readlines()
    for line in lines:
        action=line[:-1].split()
        print (action)
        moveCrates(int(action[1]),int(action[3]),int(action[5]))

print(crates)
