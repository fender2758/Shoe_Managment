from shapely.geometry import Polygon, mapping, Point
from shapely.geometry import LineString

import pygame

import numpy as np

class shoe:
    def __init__(self, ID, LR, shape, __type):
        self.ID = ID
        self.LR = LR
        self.pos = Polygon(shape)
        self.state = ""
        self.type = __type

    def spin(self, point, angle):
        block = mapping(self.pos)
        pos = block['coordinates'][0][:-1]
        af_pos = []
        for p in pos:
            x, y = p
            length = np.sqrt((x-point[0])**2+(y-point[1]**2))
            __angle = np.arcsin((y-point[1])/length)
            __angle += angle
            x = point[0] + length * np.cos(__angle)
            y = point[0] + length * np.sin(__angle)
            af_pos.append((x, y))

        self.pos = Polygon(af_pos)

        return 0

    def move(self, angle, speed):
        block = mapping(self.pos)
        pos = block['coordinates'][0][:-1]
        af_pos = []
        for p in pos:
            x, y = p
            x = x + speed * np.cos(angle)
            y = x + speed * np.sin(angle)
            af_pos.append((x, y))

        self.pos = Polygon(af_pos)


    def get_center(self):
        block = mapping(self.pos.centroid)

        return block['coordinates']

    def draw(self, screen):
        block = mapping(self.pos)
        pos = block['coordinates'][0][:-1]
        shape = []
        for p in pos:
            x = p[0]*10
            y = p[1]*10

            shape.append([x, y])
        if self.LR == "left":
            pygame.draw.polygon(screen, (255, 0, 0), shape)
        if self.LR == "right":
            pygame.draw.polygon(screen, (0, 255, 0), shape)

