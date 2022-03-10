import time


class Node():
    def __init__(self, parent = None, position = 0):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position



def a_star(level, start, end):#this function will return the path
    
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    openList = []
    closedList = []
    openList.append(startNode)

    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index 
            
        openList.pop(currentIndex)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = [] #skapar vägen
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            print("Steps taken...: ", len(path))
            return path[::-1]


        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])

            if node_position[0] > (len(level) - 1) or node_position[0] < 0 or node_position[1] > (len(level[len(level) - 1]) -1) or node_position[1] < 0:
                continue
            if level[node_position[1]][node_position[0]] != 0:
                continue

            newNode = Node(currentNode, node_position)
            newNode.g = currentNode.g + 1
            newNode.h = (abs(newNode.position[0] - endNode.position[0]) ) + (abs(newNode.position[1] - endNode.position[1]) )
            newNode.f = newNode.g + newNode.h

            try:
                closedList.index(newNode)
                continue
            except ValueError:
                pass

            try:
                nodeIndex = openList.index(newNode)
                currentChild = openList[nodeIndex]
                if currentChild.g > newNode.g:
                    openList[nodeIndex] = newNode
            except ValueError:
                openList.append(newNode)

                




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
    
    for rowIndex, row in enumerate(map):
        for col, char in enumerate(row):
            if char == 2:
                startNode = (col,rowIndex)
                
            if char == 3:
                endNode = (col,rowIndex)
    
    map[startNode[1]][startNode[0]] = 0
    map[endNode[1]][endNode[0]] = 0



    
    run = a_star(map, startNode, endNode)

    t0 = time.perf_counter()
    print(run)
    t1 = time.perf_counter() - t0
    print("time elapsed: ", t1)

    
    for position in run:
        line = lines[position[1]]
        lines[position[1]] = line[:position[0]] + "P" + line[position[0]+1:]
        
        
    for position in run:
        line = lines[position[1]]
        lines[position[1]] = line.replace("P", "\x1b[1;32mP\x1b[0m")
        

    for position in run:
        line = lines[position[1]]
        lines[position[1]] = line.replace("X", "\x1b[1;31mX\x1b[0m")


    print('\n'.join(lines))
    
    
if __name__ == '__main__':
    main()

