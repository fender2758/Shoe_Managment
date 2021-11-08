from shapely.geometry import Polygon, mapping, Point

import pygame


class ParkingSlot():
    def __init__(self, pos):
        self.pos = Polygon(pos)

    def check(self, pos):
        if self.pos:
            return


class EntMap():
    def __init__(self):
        self.map = None
        self.parkingslots = []
        self.full_parkingslots = []

    def map_gen(self):
        self.map = Polygon([(0, 0), (0, 40), (40, 40), (40, 0)])

    def parking_gen(self):
        self.parkingslots = [Polygon([(0, 0), (15, 0), (15, 30), (0, 30)]),
                             Polygon([(15, 0), (25, 0), (25, 30), (15, 30)])]
        return 0

    def get_parkingslot(self, index=-1):
        if index == -1:
            return self.parkingslots
        else:
            return self.parkingslots[index]

    def park(self):
        self.full_parkingslots.append(self.parkingslots[0])
        self.parkingslots.pop(0)

    def get_parkingslots(self):
        pass

    def draw(self, screen):
        for p in self.parkingslots:
            block = mapping(p)
            pos = block['coordinates'][0][:-1]
            shape = []
            for p in pos:
                x = p[0]*10
                y = p[1]*10

                shape.append([x, y])
            pygame.draw.polygon(screen, (0, 0, 0), shape, 3)
