from numpy import random
import pygame
import time


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position




def updateGrid(coordinate, grid):
    grid[coordinate[1]][coordinate[0]]=1
    



def drawGrid():
    blockSize = 20 
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)







def handleClick(grid):
    clicks=0
    
 
   
    while True:
        for event in pygame.event.get():
          
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clicks == 0:
                    clicks=clicks+1
                    x,y=event.pos
                    start=y // 20, x // 20
                    rectangle = pygame.Rect(start[1]*20, start[0]*20, 20, 20)
                    pygame.draw.rect(SCREEN, RED, rectangle)
                    continue
                  
                if clicks == 1:
                    clicks=clicks+1
                    x,y=event.pos
                    end=y // 20, x // 20
                    rectangle = pygame.Rect(end[1]*20, end[0]*20, 20, 20)
                    pygame.draw.rect(SCREEN, GREEN, rectangle)
                    continue
                  

                if clicks > 1:
                    x,y = event.pos
                    coordinate = x // 20, y // 20
                    rectangle = pygame.Rect(coordinate[0]*20, coordinate[1]*20, 20, 20)
                    updateGrid(coordinate,grid)
                    pygame.draw.rect(SCREEN, BLACK, rectangle)



            if event.type == pygame.KEYDOWN:
                
                path = Algorithm(grid, start, end)
                
                
                for axis in path:
                    rectangle = pygame.Rect(axis[1]*20, axis[0]*20, 20, 20)
                    pygame.draw.rect(SCREEN, PURPLE, rectangle)
                    time.sleep(0.1)
                    pygame.display.update()
                 
                time.sleep(3)
                pygame.quit()
                exit() 
                    

               
            pygame.display.update()   
               






def constructPath(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1] 


def Algorithm(grid, start, end):
    
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    open_list = []
    closed_list = []

  
    open_list.append(startNode)

   
    while len(open_list) > 0:

       
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

    
        if current_node == endNode:
            return constructPath(current_node)
           
     
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: 

        
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                continue

         
            if grid[node_position[0]][node_position[1]] != 0:
                continue

        
            new_node = Node(current_node, node_position)

       
            children.append(new_node)

       
        for child in children:

         
            for closed_child in closed_list:
                if child == closed_child:
                    continue

       
            child.g = current_node.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

          
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            
            open_list.append(child)




def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("A star simulation")
    SCREEN.fill(WHITE)

    rows, cols = (40, 40)
    grid = [[0 for i in range(cols)] for j in range(rows)]
 
        
    drawGrid()
    handleClick(grid)

   

if __name__ == "__main__":
    main()
