import pygame
import random
import time
import neat
import os

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("AI plays Snake")


class Snake:
    pass


def window_draw(win):
    win.fill(50, 50, 50)


def main(genomes=None, config=None):
    FPS = 30

    if genomes is None:
        pass

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        window_draw(win)
        pygame.display.update()


def run(conf_p):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, conf_p)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(main, 50)


if __name__ == '__main__':
    '''
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
    '''
    main()
