# -*- coding: utf-8 -*-
import os, sys
import getopt

images_dir = os.path.join( "/home/lorrany/AstroMoon/", "images" )
image_fog= "fog.png"
night_back = "tile640.png"

import pygame
from pygame.locals import *


class Background:

    #attribute that will be a background of the game
    image = None
    pos = None

    def __init__( self ):

        pygame.init()
        #logo
        logo_icon = os.path.join(images_dir, image_fog)
        logo_icon = pygame.image.load(logo_icon)
        pygame.display.set_icon(logo_icon)
        pygame.display.set_caption("AstroMoon")

        #screen
        screen = pygame.display.set_mode((600,600))
        screen.fill((255,255,255))
        nigth = os.path.join(images_dir, night_back)
        nigth = pygame.image.load(nigth)
        screen.blit(nigth, (0,0))
        pygame.display.flip()

    #def draw(self, screen):
     #   screen.blit(self.image, (0,0))

class Game:

    screen = None
    screen_size = None
    running = True
    background = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def loop(self):

        self.background = Background()

        while self.running:
            self.handle_events()

def main():
    game = Game()
    game.loop()

if __name__ =="__main__":
    main()