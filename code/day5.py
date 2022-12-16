crates=[]
sequence=[]

def buildCrates():
    global crates

    l1=['S','M','R','N','W','J','V','T']
    l2=['B','W','D','J','Q','P','C','V']
    l3=['B','J','F','H','D','R','P']
    l4=['F','R','P','B','M','N','D']
    l5=['H','V','R','P','T','B']
    l6=['C','B','P','T']
    l7=['B','J','R','P','L']
    l8=['N','C','S','L','T','Z','B','W']
    l9=['L','S','G']

    crates.append(l1)
    crates.append(l2)
    crates.append(l3)
    crates.append(l4)
    crates.append(l5)
    crates.append(l6)
    crates.append(l7)
    crates.append(l8)
    crates.append(l9)

def executeSequence(qty,frm,to):
    print(qty, frm, to)
    for _ in range(qty):
        x=crates[frm-1].pop()
        crates[to-1].append(x)  

def loadSequence():
    global sequence
    with open("/home/sree/Documents/aoc/day5.txt") as fp:
        Lines = fp.readlines()
        for line in Lines:
            seq=line[:-1].split(" ")
            executeSequence(int(seq[1]),int(seq[3]),int(seq[5]))
buildCrates()
loadSequence()
print(crates)
# print(crates[2], crates[8])
# executeSequence(7,3,9)
# print(crates[2], crates[8])
