import pygame as py, sys
import numpy as np
from constants import *
import random 
class Tiles:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = np.zeros((ROWS, COLS))
        self.lbl_font = py.font.SysFont('Arial', 25, bold= True)

    def draw(self):
        rowShift, columnShift = GAP,GAP
        for row in range(ROWS):
            for col in range (COLS):
                tile_num = int(self.tiles[row][col])

                #Tile
                tile_color = TILES_COLORS[tile_num]
                py.draw.rect(self.screen, tile_color, (27 + columnShift + col * TILE_SIZE, 227 + rowShift + row * TILE_SIZE, TILE_SIZE,TILE_SIZE), border_radius = 6)
        
                lbl = self.lbl_font.render(str(tile_num), 0, 'black')
                lbl_pos = (27 + columnShift + col * TILE_SIZE + TILE_SIZE//2 - lbl.get_rect().width//2,
                227 + rowShift + row * TILE_SIZE + TILE_SIZE//2 - lbl.get_rect().height//2
                )
                if tile_num > 0:
                    self.screen.blit(lbl,lbl_pos)
                columnShift += GAP
            rowShift += GAP
            columnShift = GAP

    def generate_tiles(self):
        empty_tiles = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.tiles[row][col] == 0: empty_tiles.append((row, col))
            tile_value = 0
            if len(empty_tiles) > 0:
                 idx = random.randrange(0, len(empty_tiles))
                 row, col =empty_tiles[idx]
                 rnd = random.randint(1,10)
                 tile_value = 2
                 if rnd > 7: tile_value = 4
        self.tiles[row][col] = tile_value

    def tile_state(self):
        return self.tiles

class Motivation:
    def __init__(self, screen):
        self.screen = screen
        self.font = py.font.SysFont('Helvetica', 25)
        self.goal = 2048
        self.title =f'Your next goal is to get to the {self.goal} tile!'

    def draw(self):
         self.screen.blit(self.font.render(self.title, True, (165,163,154)), (35, 175))

        
class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = py.Rect(20,220, background_width - 40, background_width-40)

    def draw(self):
        py.draw.rect(self.screen, foreground, self.board, border_radius=4)
    
class Score:

    def __init__(self, screen, title, xpos,):
        self.screen = screen
        self.score = py.Rect(xpos , 20, 105, 110)
        self.xpos = xpos
        self.title = title
        self.font = py.font.SysFont('Helvetica', 20, True)

    def draw(self):
         py.draw.rect(self.screen, foreground, self.score, border_radius=3)
         self.screen.blit(self.font.render(self.title, True, (247,237,227)), (self.xpos+25, 30))
       
class GUI:
    
    def __init__(self, screen):
        #Screen
        self.screen = screen

        #logo
        self.logo = py.image.load("2048_logo.png")
        self.logo = py.transform.scale(self.logo, (125, 125))
        
        #Score and Best score blocks
        self.best_score = Score(screen,'BEST', background_width - 120)
        self.score = Score(screen, 'SCORE', background_width - 240)

        #make the text above the board
        self.text = Motivation(screen)
        # make the surface of the board
        self.board = Board(screen)
       
    def show_start(self):
        self.screen.blit(self.logo,(20,20))
        self.best_score.draw()
        self.score.draw()
        self.text.draw()
        self.board.draw()
       
        
class Game:

    def __init__(self, screen):  
        self.screen = screen
        self.tiles = Tiles(screen)
        self.gui= GUI(screen)

    def draw_board(self):
        self.tiles.draw()
    
    def generate_tiles(self):
        self.tiles.generate_tiles()

def main():
    py.init()
     #will use this to make animation move relative to actual time
    clock = py.time.Clock()
    #initalize the screen
    screen = py.display.set_mode((background_width,background_height))
    #create the game object
    game = Game(screen)

    screen.fill((background_color))
    game.gui.show_start()
    n = 2
    for i in range(n): game.generate_tiles()
    #game loop
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
       
        #fill screen and show start screen
        game.draw_board()
        
        py.display.flip()
        
if __name__ == '__main__':
    main()