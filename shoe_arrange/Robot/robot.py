import numpy as np
from shapely.geometry import Polygon, mapping, Point
from shapely.geometry import LineString
from Shoes.Shoe import shoe
import pygame


class Robot:
    def __init__(self):
        self.shape = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
        self.shoe = None
        self.shoe_on = False

    def spin(self, angle, point = None):
        block = mapping(self.shape)
        pos = block['coordinates'][0][:-1]
        if not point:
            point = ((pos[2][0]+pos[3][0])/2, (pos[2][1]+pos[3][1])/2)
        print(point)
        af_pos = []
        for p in pos:
            x, y = p
            length = np.sqrt((x - point[0]) ** 2 + (y - point[1]) ** 2)

            __angle = np.arcsin((y - point[1]) / length)
            if x - point[0] < 0:
                __angle = np.pi - np.arcsin((y - point[1]) / length)

            __angle += angle
            print(x, y, length, __angle)
            x = point[0] + length * np.cos(__angle)
            y = point[1] + length * np.sin(__angle)
            af_pos.append((x, y))
        af_pos.append(af_pos[0])
        print(af_pos)
        self.shape = Polygon(af_pos)

        return 0

    def move(self, angle, speed):
        block = mapping(self.shape)
        pos = block['coordinates'][0][:-1]
        af_pos = []
        for p in pos:
            x, y = p
            x = x + speed * np.cos(angle)
            y = y + speed * np.sin(angle)
            af_pos.append((x, y))
        af_pos.append(af_pos[0])

        self.shape = Polygon(af_pos)

    def take_shoe(self, __shoe):
        self.shoe = __shoe
        self.shoe_on = True
        x, y = self.shoe.pos


    def release_shoe(self):
        self.shoe = None
        self.shoe_on = False

    def activate_robot(self, env):
        """
        자동차 프로세스
        주차하고 여행을 떠남
        parking 과 driving 상태를 스위칭함
        """
        while True:
            print('Start parking at %d pos: ' % env.now)
            block = mapping(self.shape)
            self.move(3.141592/2, 0.3)
            self.spin(0.1)
            parking_duration = 5
            yield env.timeout(parking_duration)

    def draw(self, screen):
        block = mapping(self.shape)
        pos = block['coordinates'][0][:-1]
        shape = []
        for p in pos:
            x = p[0]*10
            y = p[1]*10

            shape.append([x, y])
        pygame.draw.polygon(screen, (0, 0, 255), shape)
