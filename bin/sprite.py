# -*- coding: utf-8 -*-
import os
import pygame


class Sprite(object):
    # yolo cutting
    coords = {'idle': (
            (0, 15),
            (49, 15),
            (99, 15),
            (148, 15)
        ), 'walking': (
            (202, 15),
            (249, 15),
            (298, 15),
            (348, 15),
            (398, 15)
        )
    }

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
        sprites = dict()
        for name, coords in self.coords.iteritems():
            sprites[name] = list()
            for coord in coords:
                rect = pygame.Rect(coord[0], coord[1], 50, 85)
                sprite = spriteset.subsurface(rect).convert()
                sprite = pygame.transform.scale2x(sprite)
                sprites[name].append(sprite)
        return sprites
