import numpy as np
maze=[]
con_maze=[]
def load_maze():
    with open("C:\Advent\data\day12x.txt") as f:
        lines = f.readlines()
        for line in lines:
            a=[ord(x) for x in line[:-1]]
            a=list(map(lambda x: x-96 if x > 96 else x-38, a))
            maze.append(a)
            print(maze)
def connected_maze():
    x=len(maze)
    y=len(maze[0])
    con_maze=np.zeros((x,y))
    print(con_maze)
    for i in range(x-1):
        for j in range(y-1):
            if ((maze[i][j+1] - maze[i][j]) == 0 or (maze[i][j+1] - maze[i][j]) == 1):
                con_maze[i][j+1]=1
            if ((maze[i+1][j] - maze[i][j]) == 0 or (maze[i+1][j] - maze[i][j]) == 1):
                con_maze[i+1][j]=1
    print(con_maze)
load_maze()
connected_maze()


