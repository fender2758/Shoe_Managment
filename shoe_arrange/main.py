import pygame
import simpy

from Generator.generator import generator

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 1024

gamepad = pygame.display.set_mode((pad_width, pad_height))
clock = pygame.time.Clock()



def runGame():
    global gamepad, clock, __Generator, env

    x = pad_width * 0.05
    y = pad_width * 0.8
    y_change = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change

        gamepad.fill(WHITE)
        __Generator.draw(gamepad)

        pygame.display.update()
        print('Tick')
        parking_duration = 1
        clock.tick(60)
        yield env.timeout(1)
    pygame.quit()
    quit()


def initGame():
    global gamepad, clock, __Generator, env
    pygame.init()
    pygame.display.set_caption('PyFlying')
    __Generator.generate()
    __Generator.activate_robot()
    env.process(runGame())
    env.run(until=10000)


if __name__ == '__main__':
    env = simpy.Environment()
    __Generator = generator(env)
    initGame()
