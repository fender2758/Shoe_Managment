from Shoes.Shoe.shoe import shoe


class shoes:
    def __init__(self, ID, shape, __type):
        self.shoes = [shoe(ID, "left", shape[0], __type), shoe(ID, "right", shape[1], __type)]
        self.type = "type"

    def draw(self, screen):
        self.shoes[0].draw(screen)
        self.shoes[1].draw(screen)

    def get_shoe(self, LR=-1):
        if LR == -1:
            return self.shoes[0], self.shoes[1]
        if LR == 0:
            return self.shoes[0]
        else:
            return self.shoes[1]
