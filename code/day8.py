forest=[]
total_trees=0
visible_trees=0
hidden_trees=0

def build_forest():
    with open("C:\Advent\data\day8.txt") as f:
        lines = f.readlines()
        for line in lines:
            tree_line=list(map(int,line.strip()))
            forest.append(tree_line)

def visible_from_left(r,c):

    x=forest[r][c-1::-1]

    print(x,r,c,"left")
    
    if ((len(x) == 0) or (max(x) < forest[r][c])):
        return True
    else:
        return False
    # print(x, forest[r][c])

def visible_from_right(r,c):
    x=forest[r][c+1:]
    print(x,r,c,"right")

    if ((len(x) == 0) or (max(x) < forest[r][c])):
        return True
    else:
        return False
    # print(x,forest[r][c])

def visible_from_bottom(r,c):
    z=[]

    for v in range (r+1, len(forest)):
        z.append(forest[v][c])

    print(z,r,c,"bottom")
    if ((len(z) == 0) or (max(z) < forest[r][c])):
        return True
    else:
        return False

def visible_from_top(r,c):
    z=[]

    for v in range (r-1,-1,-1):
         z.append(forest[v][c])
    
    if ((len(z) == 0) or (max(z) < forest[r][c])):
        return True
    else:
        return False

def visible_count(treelist,k):
    count=0
    for h in treelist:
       count+=1
       if (h>=k):
        break;
    print (count,treelist,k)
    return count

def left_score(r,c):

    x=forest[r][c-1::-1]

    return visible_count(x,forest[r][c])


def right_score(r,c):
    
    x=forest[r][c+1:]
    return visible_count(x,forest[r][c])

def top_score(r,c):
    
    z=[]
    for v in range (r-1,-1,-1):
         z.append(forest[v][c])

    return visible_count(z,forest[r][c])

def bottom_score(r,c):
    z=[]

    for v in range (r+1, len(forest)):
        z.append(forest[v][c])

    return visible_count(z,forest[r][c])

def part1():
    total_trees = len(forest) * len(forest[0])
    # is_tree_visible(1,3)
    for r in range(len(forest)):
        for c in range(len(forest)):
            if  (r==0 or c==0 or r==len(forest) or c==len(forest)):
                pass
            elif (visible_from_left(r,c) or visible_from_right(r,c) or visible_from_top(r,c) or visible_from_bottom(r,c)):
                pass
            else:
                hidden_trees+=1

    print(total_trees, hidden_trees, (total_trees-hidden_trees))
def part2():
    highest_score=0
    tree_score=0
    for r in range(len(forest)):
        for c in range(len(forest)):
            if  (r==0 or c==0 or r==len(forest) or c==len(forest)):
                pass
            else:
                tree_score=0
                tree_score=(left_score(r,c)) * (right_score(r,c)) * (top_score(r,c)) * (bottom_score(r,c))
                print(r,c,tree_score)
                if (tree_score>highest_score):
                    highest_score=tree_score
    print(highest_score)
            

build_forest()
part2()



