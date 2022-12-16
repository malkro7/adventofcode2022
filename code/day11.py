from math import trunc
import cProfile
monkeys=[]
monkey_business={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
modulus=2*7*13*3*19*17*11*5
# modulus=23*19*13*17
print(modulus)
def prepareRounds():
    l0=[84, 66, 62, 69, 88, 91, 91]
    l1=[98, 50, 76, 99]
    l2=[72, 56, 94]
    l3=[55, 88, 90, 77, 60, 67]
    l4=[69, 72, 63, 60, 72, 52, 63, 78]
    l5=[89, 73]
    l6=[78, 68, 98, 88, 66]
    l7=[70]
    monkeys.append({"items":l0, "oper": "*", "val": 11, "div": 2, "succ":4, "fail":7})
    monkeys.append({"items":l1, "oper": "*", "val":"item", "div": 7, "succ":3, "fail":6})
    monkeys.append({"items":l2, "oper": "+", "val":1, "div": 13, "succ":4, "fail":0})
    monkeys.append({"items":l3, "oper": "+", "val":2, "div": 3, "succ":6, "fail":5})
    monkeys.append({"items":l4, "oper": "*", "val":13, "div": 19, "succ":1, "fail":7})
    monkeys.append({"items":l5, "oper": "+", "val":5, "div": 17, "succ":2, "fail":0})
    monkeys.append({"items":l6, "oper": "+", "val":6, "div": 11, "succ":2, "fail":5})
    monkeys.append({"items":l7, "oper": "+", "val":7, "div": 5, "succ":1, "fail":3})
def prepareTestRounds():
    l0=[79, 98]
    l1=[54, 65, 75, 74]
    l2=[79, 60, 97]
    l3=[74]
    monkeys.append({"items":l0, "oper": "*", "val": 19, "div": 23, "succ":2, "fail":3})
    monkeys.append({"items":l1, "oper": "+", "val": 6,  "div": 19, "succ":2, "fail":0})
    monkeys.append({"items":l2, "oper": "*", "val": "item", "div": 13, "succ":1, "fail":3})
    monkeys.append({"items":l3, "oper": "+", "val":3, "div": 17, "succ":0, "fail":1})
def playRound():
    for i in range(len(monkeys)):
        startingItems=monkeys[i].get("items")
        operator=monkeys[i].get("oper")
        value=monkeys[i].get("val")
        divisor=monkeys[i].get("div")
        goodMonkey=monkeys[i].get("succ")
        badMonkey=monkeys[i].get("fail")
        counter=0
        for item in startingItems:
            counter+=1
            if (operator=="*"):
                if (value == "item"):
                    # worryLevel=trunc((int(item)**2)/3)
                    worryLevel=int(item)*int(item)
                else:
                    # worryLevel=trunc((int(item)*value)/3)
                    worryLevel=int(item)*value
            elif (operator=="+"):
                # worryLevel=trunc((item+value)/3)
                worryLevel=item+value

            if ((worryLevel%divisor) == 0):
                monkeys[goodMonkey].get("items").append(worryLevel%modulus)
            else:
                monkeys[badMonkey].get("items").append(worryLevel%modulus)
        monkey_business[i]=monkey_business.get(i) + counter
        for _ in range(counter):
            monkeys[i].get("items").pop(0)
        
        # print(monkeys)
prepareRounds()
with cProfile.Profile() as pr:
    for _ in range(10000):
        playRound()
    mb=list(monkey_business.values())
    mb=sorted(mb)
    x=mb.pop()
    y=mb.pop()
    print(x,y)
    print(x*y)
pr.print_stats()