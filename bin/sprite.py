# -*- coding: utf-8 -*-
import os
import pygame


class Sprite(object):
    def build_spriteset(self):
        """
        Cut and build sprite set
        """
        # get spriteset
        path = os.path.dirname(os.path.realpath(__file__))
        spriteset = pygame.image.load(path + '/../assets/ryu.gif').convert()
        transparent_pixel = (0, 0)
        spriteset.set_colorkey(
            spriteset.get_at(transparent_pixel)
        )
        sprites = list()
        # yolo cutting
        rect = pygame.Rect(0, 10, 50, 90)
        sprite = spriteset.subsurface(rect).convert()
        sprite = pygame.transform.scale2x(sprite)
        sprites.append(sprite)
        return sprites
