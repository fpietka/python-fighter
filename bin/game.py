# -*- coding: utf-8 -*-
import os
import pygame
from pygame.locals import *
from sprite import Sprite
import itertools


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
        self.walking = False
        self.sprites = Sprite().build_spriteset()

    def run(self):
        """
        Main loop
        """
        running = True
        self.sprite = itertools.cycle(self.sprites['idle'])
        self.p1left = 0
        while running:
            pygame.time.Clock().tick(10)
            running = self.handleEvents()
            # blit the background
            self.screen.blit(self.background, self.position)
            # blit the sprite
            self.screen.blit(self.sprite.next(), (self.p1left, 250))
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
        move = 'idle'
        if pressed[pygame.K_LEFT]:
            move = 'left'
            self.p1left -= 9
            """
            self.position[0] = max(
                self.position[0] - 3,
                -self.background.get_width() + self.size[0]
            )
            """
        if pressed[pygame.K_RIGHT]:
            move = 'right'
            self.p1left += 9
            """
            self.position[0] = min(self.position[0] + 3, 0)
            """
        if move in ('left', 'right'):
            if not self.walking:
                self.walking = True
                self.sprite = itertools.cycle(self.sprites['walking'])
        else:
            if self.walking:
                self.walking = False
                self.sprite = itertools.cycle(self.sprites['idle'])
        return True
