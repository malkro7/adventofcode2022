direction=[]
steps=[]
head_steps=[]
tail_movement=[]
tail_steps=[]

def load_movement():
    with open("C:\Advent\data\day9x.txt") as f:
        lines = f.readlines()
        for line in lines:
            x,y=line.strip().split()
            direction.append(x)
            steps.append(int(y))
            
def map_head_movement():
    head_x=0
    head_y=0
    tail_x=0
    tail_y=0
    head_steps.append((head_x,head_y))
    tail_steps.append((head_x,head_y))

    for l in range(len(direction)):
        i=direction[l]
        j=steps[l]
        for x in range(1,j+1):
            if   (i=='R'):
                head_x += 1
            elif (i=='L'):
                head_x -= 1
            elif (i=='U'):
                head_y += 1
            elif (i=='D'):
                head_y -= 1
            else:
                raise ValueError
            head_steps.append((head_x,head_y))
    print(len(head_steps),head_steps)

def map_tail_movement():
    tail_x=tail_steps[-1][0]
    tail_y=tail_steps[-1][1]

    for xy in head_steps:
        head_x=xy[0]
        head_y=xy[1]

        if ((head_x!=tail_x) and (head_y != tail_y)):
                change_in_axis = True

        if (abs(head_x-tail_x) > 1):
            if (change_in_axis):
                tail_y=head_y
                tail_x +=1
            elif (head_x < tail_x):
                tail_x -=1
            else:
                tail_x +=1
        if (abs(head_y-tail_y) > 1):            
            if (change_in_axis):
                tail_x=head_x
                tail_y+=1
            elif (head_y < tail_y):
                tail_y-=1
            else:
                tail_y +=1
        print(xy, tail_x, tail_y)
        tail_steps.append((tail_x,tail_y))
        change_in_axis = False

# load_movement()
# map_head_movement()
# map_tail_movement()
# print(tail_steps)
v = set( [ ( 0, 0 ) ] )
x, y = [ 0 ] * 10, [ 0 ] * 10
with open("C:\Advent\data\day9.txt") as f:
    lines = f.readlines()
for l in lines:
    a, n = l.split()
    print(a,n)
    for i in range( int( n ) ):
        x[ 0 ] += { "U": 0, "R": 1, "D": 0, "L": -1 }[ a ]
        y[ 0 ] += { "U": -1, "R": 0, "D": 1, "L": 0 }[ a ]
        for k in range( 1, len( x ) ):
            while ( abs( x[ k ] - x[ k - 1 ] ) > 1 or
                    abs( y[ k ] - y[ k - 1 ] ) > 1 ):
                x[ k ] += ( x[ k - 1 ] > x[ k ] ) - ( x[ k - 1 ] < x[ k ] )
                y[ k ] += ( y[ k - 1 ] > y[ k ] ) - ( y[ k - 1 ] < y[ k ] )
        v.add( ( x[ -1 ], y[ -1 ] ) )
print( len( v ) )
