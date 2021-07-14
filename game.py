import pygame
import random
import time
from pygame.locals import *
import PIL
from PIL import Image

im = Image.open("resources/board.jpg")
im1 = Image.open("resources/cross.jpg")
block = im1.size[0]
Grid_X = im.size[0]
Grid_Y = im.size[1]
BG_color = (250,250,250)
text = (106,13,173)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((Grid_X,Grid_Y))
        self.surface.fill(BG_color)
        self.board = pygame.image.load("resources/board.jpg").convert_alpha()
        self.cross = pygame.image.load("resources/cross.jpg").convert_alpha()
        self.circle = pygame.image.load("resources/circle.jpg").convert_alpha()
        self.state = [['?','?','?'],['?','?','?'],['?','?','?']]
    
    def start_screen(self):
        self.surface.fill(BG_color)
        font = pygame.font.SysFont('arial', 15)
        line1 = font.render(f"Press c to play with computer", True, text)
        self.surface.blit(line1,(100,100))
        line2 = font.render(f"Press p to play with player", True, text)
        self.surface.blit(line2,(100,150))
        pygame.display.flip()
    
    def draw_board(self):
        self.surface.fill(BG_color)
        self.surface.blit(self.board,(0,0))
        pygame.display.flip()
    
    def draw(self,image,point):
        x = (Grid_X // 6) + ((Grid_X // 3) * point[0])
        y = (Grid_Y// 6) + ((Grid_Y // 3) * point[1])
        self.surface.blit(image,(x - (block // 2),y - (block // 2)))
        pygame.display.flip()

    
    def draw_move(self,image,point):
        x = point[0]
        y = point[1]
        mod_x = 0
        mod_y = 0
        if (x < Grid_X // 3):
            mod_x = 0
        elif (x < 2*Grid_X // 3):
            mod_x = 1
        else:
            mod_x = 2
        if (y < Grid_Y // 3):
            mod_y = 0
        elif (y < 2*Grid_Y // 3):
            mod_y = 1
        else:
            mod_y = 2
        print(mod_x,mod_y)
        if image == self.cross:
            self.state[mod_x][mod_y] = 'x'
        else:
            self.state[mod_x][mod_y] = 'o'
        self.draw(image,(mod_x,mod_y))
    
    def player_move(self,player,image):
        pos = pygame.mouse.get_pos()
        self.draw_move(image,pos)
    
    def game_end(self,who):
        self.surface.fill(BG_color)
        font = pygame.font.SysFont('arial', 15)
        if (who == 'x'):
            line1 = font.render("cross wins!", True, text)
        else:
            line1 = font.render("circle wins!", True, text)
        self.surface.blit(line1,(100,100))
        line2 = font.render(f"Press Enter return to main screen", True, text)
        self.surface.blit(line2,(100,150))
        pygame.display.flip()
    
    def check_win(self):
        # check rows
        for i in range(3):
            if self.state[i][0] == self.state[i][1] and self.state[i][0] == self.state[i][2] and self.state[i][1] != '?':
                self.game_end(self.state[i][0])
                return True
        # check columns
        for i in range(3):
            if self.state[0][i] == self.state[1][i] and self.state[0][i] == self.state[2][i] and self.state[0][i] != '?':
                self.game_end(self.state[0][i])
                return True
        # check diagonals
        if self.state[0][0] == self.state[1][1] and self.state[0][0] == self.state[2][2] and self.state[2][2] != '?':
            self.game_end(self.state[0][0])
            return True
        if self.state[0][2] == self.state[1][1] and self.state[0][2] == self.state[2][0] and self.state[1][1] != '?':
            self.game_end(self.state[0][2])
            return True
        return False

    def reset(self):
        self.state = [['?','?','?'],['?','?','?'],['?','?','?']]

    def run(self):
        start = True
        running = True
        turn = 0
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_c or event.key == K_p:
                        start = False
                        game.draw_board()
                    if start == True:
                        if event.key == K_RETURN:
                            self.start_screen()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if not start:
                        if turn == 0:
                            game.player_move("player1",game.circle)
                        else:
                            game.player_move("player2",game.cross)
                        turn = (turn + 1)%2
                        if game.check_win() == True:
                            start = True
                            self.reset()
                            turn  = 0



    
        

        
    
if __name__ == "__main__":
    game = Game()
    game.start_screen()
    game.run()
                
