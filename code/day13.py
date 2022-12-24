# def looplist(x):
#     print(type(x))
#     if type(x) is list:
#         looplist(x[0])
#     else:
#         print(x)
# a=[[[[[[9]]]]]]
# b=[1,[2,[3,[4,[5,6,7]]]],8,9]
# for items in b:
#     print(looplist(items))
def loadPackets():
    with open("data\day13x.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        return lines

def compare(x, y):
    if (len(x) > len(y)):
        return False
    while len(x) > 0 and len(y) > 0:
        l=x.pop(0)
        r=y.pop(0)
        if (type(l) is int and type(r) is int):
            if (l > r): 
                return False
        if (type(l) is int and type(r) is list):
            compare(list([l]),r)
        if (type(l) is list and type(r) is list):
            compare(l,r)
        if (type(l) is list and type(r) is int):
            compare(l, list([r]))
    return True
input=loadPackets()
print(type(input))
loc=[]
i=0
while len(input) > 0:
    j=eval(input.pop(0))
    k=eval(input.pop(0))
    if (len(input)>0):
        z=input.pop(0) # empty line
    if compare(j, k):
        pass
    else:
        loc.append(i)
        i+=1

print(sum(loc))
