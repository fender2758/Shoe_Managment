from Shoes.shoes import shoes
from Shoes.Shoe.shoe import shoe

from Map.Map import EntMap
from Robot.robot import Robot

import simpy

class generator:
    def __init__(self, env):
        self.map = EntMap()
        self.shoes = []
        self.pair_slot = []
        self.robot = Robot()
        self.shoes_list = []
        self.env = env

    def generate(self):
        self.map.map_gen()
        self.map.parking_gen()
        self.detect_shoe()
        self.schedule()

    def detect_shoe(self):
        self.shoes.append(
            shoes(0, [[(0, 0), (10, 0), (10, 30), (0, 30)], [(10, 0), (20, 0), (20, 30), (10, 30)]], "sneakers"))

        if 2 * len(self.shoes) > len(self.map.get_parkingslot()):
            return False

    def schedule(self):
        # shoe order

        for i, sh in enumerate(self.shoes):
            for j, s in enumerate(sh.get_shoe()):
                self.pair_slot.append((s, self.map.get_parkingslot(2 * i + j)))

        for i, sh in enumerate(self.shoes):
            for j, s in enumerate(sh.get_shoe()):
                self.shoes_list.append((s.get_center(), i, j))

        sorted(self.shoes_list, key=lambda x: (x[0][0], x[0][1]))

    def activate_robot(self):
        self.env.process(self.robot.activate_robot(self.env))
        self.env.run(until=15)

        return 0

    def draw(self, screen):
        self.map.draw(screen)
        for sh in self.shoes:
            sh.draw(screen)
        self.robot.draw(screen)
