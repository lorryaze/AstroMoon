# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

class Background:

    #attribute that will be a background of the game
    image = None

    #constructor for a instance of Background
    def __init__( self ):
        #image that will be set to the background of game
        #screen = pygame.display.get_surface()
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
        logo_icon = pygame.image.load("fog.png")
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