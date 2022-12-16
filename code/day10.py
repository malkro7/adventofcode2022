signal_register=[]
X=1
def part1():
    with open("C:\Advent\data\day10.txt") as f:
        lines = f.readlines()
    for line in lines:
        try:
            action, value = line.split()
            print (action, int(value))
        except(ValueError):
            action=line.strip()
            print(action)
        if (action == "noop"):
            pass
        else:
            signal_register.append(X)
            X+=int(value)
        signal_register.append(X)
def part2():
    sprite_pos=0
    X=1
    with open("C:\Advent\data\day10.txt") as f:
        lines = f.readlines()
    for line in lines:
        try:
            action, value = line.split()
            no_cycle=2
        except(ValueError):
            action=line.strip()
            no_cycle=1
            value=0
        # print(action, no_cycle)
        for i in range(no_cycle):
            if X in (sprite_pos-1, sprite_pos, sprite_pos+1):
                print('@',end='')
            else:
                print('.',end='')
            sprite_pos +=1
            if (sprite_pos==40):
                print()
                sprite_pos=0
        X+=int(value)
        
part2()
# part1()
# print(signal_register)
# print(signal_register[18]*20,signal_register[58]*60,signal_register[98]*100,signal_register[138]*140,signal_register[178]*180,signal_register[218]*220)
# print(signal_register[18]*20+signal_register[58]*60+signal_register[98]*100+signal_register[138]*140+signal_register[178]*180+signal_register[218]*220)
    
        
#         action="noop"
# for i in range(2):
#     if (action=="noop"):
#         mylist.append(x)
#         action="addx"
#     else:
#         mylist.append(mylist[-1])
#         mylist.append(mylist[-1]+3)
# print(mylist)