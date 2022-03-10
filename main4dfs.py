import time

pathSoFar = []

def dfs(level, startY, startX, goal):
    if startY < 0 or startX < 0 or startY > len(level)-1 or startX > len(level[0]) - 1:
        return
        
    #if we been there or there is a wall, quit
    if (startY, startX) in pathSoFar or level[startY][startX] > 0:

        return
    
    pathSoFar.append((startY,startX))
    level[startY][startX] = 2

    if (startY, startX) == goal:
        print("FOund!: ", pathSoFar)
        print("Steps taken...: ",len(pathSoFar))

        pathSoFar.pop()
        return
    else:
        dfs(level, startY - 1, startX, goal) #top
        dfs(level, startY + 1, startX, goal) #bot
        dfs(level, startY, startX + 1, goal) #right
        dfs(level, startY, startX - 1, goal) #left
    



def mapChar(char):
    if char == "X":
        return 1
    elif char == "S":
        return 2
    elif char == "G":
        return 3
    else:
        return 0

def mapLine(line):
    return [mapChar(char) for char in line]


def main():


    f = open("map3.txt", "r")
    lines = (f.read().splitlines())
    map = [mapLine(line) for line in lines]
    # print(map)
    
    for rowIndex, row in enumerate(map):
        for col, char in enumerate(row):
            if char == 2:
                startNode = (col,rowIndex)
                
            if char == 3:
                endNode = (col,rowIndex)
    
    map[startNode[0]][startNode[1]] = 0
    map[endNode[0]][endNode[1]] = 0


    
    t0 = time.perf_counter()
    dfs(map, startNode[1], startNode[0], endNode)
    t1 = time.perf_counter() - t0
    print("time elapsed: ", t1)


if __name__ == '__main__':
    main()




