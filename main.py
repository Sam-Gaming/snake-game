import pygame
from pygame.locals import *

Class Game():
    def _init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((1000,500))
        self.snake=Snake(self.surface)       
        self.snake.draw()


    def run(self):
        
        running=True

        while running:
           for event in pygame.event.get():
             if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False
                if event.key==K_UP:
                    block_y=block_y-10
                    draw_block()

                if event.key==K_DOWN:
                    block_y=block_y+10
                    draw_block()

                if event.key==K_LEFT:
                    block_x=block_x-10
                    draw_block()

                if event.key==K_RIGHT:
                    block_x=block_x+10
                    draw_block()

            elif event.type==QUIT:
                running=False


Class Snake():
     def __init__(self, parent_screen):
        self.parent_screen=parent_screen
        self.block=pygame.image.load("D:\Coding\Snake Game/block.jpg").convert()
        self.x=100
        self.y=100

    def draw (self):
        self.parent_screen.fill((32, 201, 193))
        self.parent_screen.blit(block,(block_x,block_y))
        pygame.display.flip()


    

if __name__=="__main__":
    game=Game()
    game.run()
    

    
    



