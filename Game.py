# -*- coding: utf-8 -*-
import os, sys
import getopt
import random
import pygame
from pygame.locals import *

images_dir = os.path.join( "/home/lorrany/AstroMoon/", "images" )
image_fog= "fog.png"
night_back = "tile640.png"
screen_width=800
screen_height=600
size = (screen_width,screen_height)

class Background:
    meteor = None
    pos_meteor = None

    def __init__( self ):

        pygame.init()
        #logo
        logo_icon = os.path.join(images_dir, image_fog)
        logo_icon = pygame.image.load(logo_icon)
        pygame.display.set_icon(logo_icon)
        pygame.display.set_caption("AstroMoon")

        #screen
        screen = pygame.display.set_mode(size)
        rock = pygame.Surface((20, 20))
        screen.fill((0, 0, 0))
        rock.fill((255, 255, 255))
        self.meteor = rock
        self.pos = (random.randint(0,590), random.randint(0,590))
        
    def draw(self, screen):
        screen.blit(self.meteor, self.pos)
        pygame.display.flip()

class Game:
    screen = None
    running = True
    background = None
    player = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def actors_draw(self, screen):
        self.player = os.path.join(images_dir, image_fog)
        self.player = pygame.image.load(self.player)
        
        xpos = 50
        ypos = 50
        step_x = 10
        step_y = 10

        self.screen = pygame.display.set_mode(size)
        #check if the fog is still on screen, if not change the direction
        if xpos > screen_width - 64 or xpos < 0:
            step_x = -step_x
        if ypos > screen_height - 64 or ypos < 0:
            step_y = -step_y
        #update the position of fog
        xpos += step_x #move it to the right
        ypos += step_y #move it to down
        #self.screen.fill((0,0,0))
        self.screen.blit(self.player, (xpos, ypos))
        pygame.display.flip()

    def loop(self):
        self.background = Background()
        self.screen = pygame.display.set_mode(size)

        while self.running:
            self.handle_events()
            self.actors_draw(self.screen)
            self.background.draw(self.screen)               
def main():
    game = Game()
    game.loop()

if __name__ =="__main__":
    main()
