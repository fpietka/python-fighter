# -*- coding: utf-8 -*-
import os
import pygame
from pygame.locals import *
from sprite import Sprite


class Game(object):
    size = (640, 480)

    def __init__(self):
        """
        Initialize the game
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        # build background
        path = os.path.dirname(os.path.realpath(__file__))
        self.background = pygame.image.load(
            path + '/../assets/background-1.jpg'
        ).convert()
        self.background = pygame.transform.scale2x(self.background)
        # calculate center
        left = (self.background.get_width() - self.size[0]) / 2
        self.position = [-left, 0]

    def run(self):
        """
        Main loop
        """
        running = True
        while running:
            pygame.time.Clock().tick(60)
            running = self.handleEvents()
            # blit the background
            self.screen.blit(self.background, self.position)
            # blit the sprite
            sprite = Sprite().build_spriteset()
            self.screen.blit(sprite[0], (0, 250))
            # update screen
            rect = pygame.Rect(
                0,
                0,
                self.size[0],
                self.size[1]
            )
            pygame.display.update(rect)

    def handleEvents(self):
        """
        Poll for pygame events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # if the user presses escape or 'q', quit the event loop.
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False
        pressed = pygame.key.get_pressed()
        # movement control controlling background for now
        if pressed[pygame.K_LEFT]:
            self.position[0] = max(
                self.position[0] - 3,
                -self.background.get_width() + self.size[0]
            )
        if pressed[pygame.K_RIGHT]:
            self.position[0] = min(self.position[0] + 3, 0)
        return True
