


def dfs(level, start, goal, path, visited):
    
    path.append(start)
    
    visited.append(start)


    if start == goal:
        return path
    
    for neightbour in level:
        if neightbour not in visited:
            result = dfs(level, neightbour, goal, path, visited)
            if result is not None:
                return result
        path.pop()
    return None
    
    



def main(): 
    
    level = [
        [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
        [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
        [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
        [1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ],
        [0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ],
        [0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ],
        [0 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],
        [0 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],
        [0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],
        [0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],  
    ]


    startNode = (0,0)
    endNode = (9,9)
    path = []
    visited = []
    dfs(level, startNode, endNode, path, visited)

if __name__ == '__main__':
    main()

