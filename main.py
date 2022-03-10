from operator import truediv
from re import X
import pygame
import os

pygame.init()

WIDTH, HEIGHT = 720, 720
rows = 20
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PATHFINDING AI")
fps = 60



def grid(WIN, WIDTH, rows):
    distanceBtwRows = WIDTH // rows
    x = 0
    y = 0

    for i in range(rows):
        #öka x och y med distanceBTWrows
        x += distanceBtwRows
        y += distanceBtwRows
        #draw grid
        pygame.draw.line(WIN, (0,255,0), (x, 0), (x, WIDTH))
        pygame.draw.line(WIN, (0,255,0), (0, y), (WIDTH, y))
    pass

def fillCell(WIN, WIDTH, rows, x, y):
    distanceBtwRows = WIDTH // rows
    x = (distanceBtwRows * x)
    y = (distanceBtwRows * y)
    cell = pygame.Rect(x ,y ,(WIDTH // rows), (WIDTH // rows))
    pygame.draw.rect(WIN, (255,255,255), cell)
    



# class Cell(WIN, WIDTH, rows):
#     def __init__(self, x, y):
#         self.x = x
#         self.x = y

#     def fillCell():
        
#         pass



def draw_window():
    WIN.fill((0,0,0))
    grid(WIN, WIDTH, rows)
    fillCell(WIN, WIDTH, rows, 4,0)
    fillCell(WIN, WIDTH, rows, 4,1)
    fillCell(WIN, WIDTH, rows, 5,2)
    fillCell(WIN, WIDTH, rows, 5,3)
    fillCell(WIN, WIDTH, rows, 4,4)
    fillCell(WIN, WIDTH, rows, 4,7)
    
    fillCell(WIN, WIDTH, rows, 4,8)
    fillCell(WIN, WIDTH, rows, 4,9)
    fillCell(WIN, WIDTH, rows, 4,9)
    fillCell(WIN, WIDTH, rows, 8,5)
    fillCell(WIN, WIDTH, rows, 8,4)
    fillCell(WIN, WIDTH, rows, 8,6)
    fillCell(WIN, WIDTH, rows, 8,7)
    fillCell(WIN, WIDTH, rows, 4,9)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    

        


        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()