from collections import Counter
def getPacketMarker(s1):
    for i in range(len(s1)-13):
        match=0
        x=s1[i:i+14:1]
        print(x)
        freq=Counter(x)
        print(freq)
        for k in x:
            if(freq[k] > 1):
                match+=1
                break
        print(match)
        if (match == 0):
            print(i+14, " is the starting position")
            break

with open("C:\Advent\data\day6.txt") as f:
    lines = f.readlines()
    for line in lines:
        getPacketMarker(line)
        
