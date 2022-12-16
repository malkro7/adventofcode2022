from math import trunc
import cProfile
monkeys=[]
monkey_business={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
def prepareRounds():
    l0=[84, 66, 62, 69, 88, 91, 91]
    l1=[98, 50, 76, 99]
    l2=[72, 56, 94]
    l3=[55, 88, 90, 77, 60, 67]
    l4=[69, 72, 63, 60, 72, 52, 63, 78]
    l5=[89, 73]
    l6=[78, 68, 98, 88, 66]
    l7=[70]
    # monkeys.append(l0, "*", 11, 2, 4, 7)
    # monkeys.append(l1, "*", "item", 7, 3, 6)
    monkeys.append({"items":l2, "oper": "+", "val":1, "div": 13, "succ":4, "fail":0})
    monkeys.append({"items":l3, "oper": "+", "val":2, "div": 3, "succ":6, "fail":5})
    monkeys.append({"items":l4, "oper": "*", "val":13, "div": 19, "succ":1, "fail":7})
    monkeys.append({"items":l5, "oper": "+", "val":5, "div": 17, "succ":2, "fail":0})
    monkeys.append({"items":l6, "oper": "+", "val":6, "div": 11, "succ":2, "fail":5})
    monkeys.append({"items":l7, "oper": "+", "val":7, "div": 5, "succ":1, "fail":3})
def prepareTestRounds():
    l0=[[79, 98],"*", 19, 23,2, 3]
    l1=[[54, 65, 75, 74],"+", 6, 19,2, 0]
    l2=[[79, 60, 97],"*", "item", 13,1, 3]
    l3=[[74],"+", 3, 17,0, 1]
    monkeys.append(l0)
    monkeys.append(l1)
    monkeys.append(l2)
    monkeys.append(l3)
def playRound():
    x=len(monkeys)
    startingItems=[]
    operator=""
    value=""
    divisor=""
    goodMonkey=""
    badMonkey=""
    counter=""
    for i in range(x):
        startingItems=monkeys[i][0]
        operator=monkeys[i][1]
        value=monkeys[i][2]
        divisor=monkeys[i][3]
        goodMonkey=monkeys[i][4]
        badMonkey=monkeys[i][5]
        counter=0
        for item in startingItems:
            counter+=1
            if (operator=="*"):
                if (value == "item"):
                    # worryLevel=trunc((int(item)**2)/3)
                    worryLevel=int(item)*int(item)
                else:
                    worryLevel=int(item)*value
            elif (operator=="+"):
                worryLevel=(item+value)

            if ((worryLevel%divisor) == 0):
                monkeys[goodMonkey][0].append(worryLevel)
            else:
                monkeys[badMonkey][0].append(worryLevel)
        monkey_business[i]=monkey_business.get(i) + counter
        for _ in range(counter):
            monkeys[i][0].pop(0)
        
        # print(monkeys)
prepareTestRounds()
with cProfile.Profile() as pr:
    for _ in range(1000):
        playRound()
    mb=list(monkey_business.values())
    mb=sorted(mb)
    x=mb.pop()
    y=mb.pop()
    print(x*y)
pr.print_stats()