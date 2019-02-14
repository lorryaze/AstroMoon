# -*- coding: utf-8 -*-
import os, sys
import getopt

images_dir = os.path.join( "/home/lorrany/AstroMoon/", "images" )
image_fog= "fog.png"

import pygame
from pygame.locals import *


class Background:

    #attribute that will be a background of the game
    image = None
    pos = None

    def __init__( self ):

       # screen = pygame.display.get_surface()
        screen = pygame.display.set_mode((600,600)).convert()

        #Create a empty pygame surface and convert surface to make blitting faster
        back = pygame.Surface(screen.get_size())
        #This function fill a background color, a python color is represent for a tuple, the (0,0,0) is black.
        back.fill((0, 0, 0))
        self.image = back

    #def draw(self, screen):
     #   screen.blit(self.image, (0,0))

class Game:

    screen = None
    screen_size = None
    running = True
    background = None

    def __init__(self):
        pygame.init()

        logo_icon = os.path.join(images_dir, image_fog)
        logo_icon = pygame.image.load(logo_icon)
        pygame.display.set_icon(logo_icon)

        pygame.display.set_caption("AstroMoon")

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