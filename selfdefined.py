from random import randint
import time


def pathfinding(level, startX, startY, goalX, goalY):
    myWay = []
    myWay.append((startY,startX))


    search = True

    while search:
        if startX == goalX and startY == goalY:
            print(myWay)
            print("I FOUND IT!!!!!!")
            print("Steps taken...: ", len(myWay))
            search = False
            break




        if startY > (len(level) - 1) or startY < 0 or startX > (len(level[len(level) - 1]) -1) or startX < 0:
            continue
        
        if level[startY][startX] != 0:
            continue


        
        choice = randint(1,4)
        if choice == 1:
            howLong = randint(1,4)
            i = 0
            try:
                while i < howLong:
                    if level[startY][startX + 1] != 1:
                        if startX >= len(level[0]):
                            break
                        startX += 1
                        myWay.append((startY,startX))

                        i += 1
                    else:
                        break
            except IndexError:
                pass
            choice = randint(1,4)

        elif choice == 2:
            howLong = randint(1,4)
            i = 0
            try:
                while i < howLong:
                    if level[startY + 1][startX] != 1:
                        if startY >= len(level):
                            break
                        startY += 1
                        myWay.append((startY,startX))

                        i += 1
                    else:
                        break
            except IndexError:
                pass
            choice = randint(1,4)

        elif choice == 3:
            howLong = randint(1,4)
            i = 0
            try:
                while i < howLong:
                    if level[startY - 1][startX] != 1:
                        if startY <= 0:
                            break
                        startY -= 1
                        myWay.append((startY,startX))

                        i += 1
                    else:
                        break
            except IndexError:
                pass
            choice = randint(1,4)
       
        elif choice == 4:
            howLong = randint(1,4)
            i = 0
            try:
                while i < howLong:
                    if level[startY][startX - 1] != 1:
                        if startX <= 0:
                            break
                        startX -= 1
                        myWay.append((startY,startX))

                        i += 1
                    else:
                        break
            except IndexError:
                pass
            choice = randint(1,4)

            

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
                    startX = col
                    startY = rowIndex 
                if char == 3:
                    goalX = col
                    goalY = rowIndex 

    map[startY][startX] = 0
    map[goalY][goalX] = 0

    
    t0 = time.perf_counter()
    pathfinding(map, startX, startY, goalX, goalY)
    t1 = time.perf_counter() - t0
    print("time elapsed: ", t1)

if __name__ == '__main__':
    main()