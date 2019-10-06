import pygame
import random
import time
import neat
import os

pygame.init()

WIN_WIDTH = 600
WIN_HEIGHT = 600

black = (50, 50, 50)
white = (255, 255, 255)
red1 = (255, 0, 0)
red2 = (200, 50, 50)
green = (50, 200, 50)

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("AI plays Snake")


class Snake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.direction = 0
        self.size = size
        self.body = [(self.x, self.y), (self.x, self.y)]  # it's doubled for purpose of ez code.

    def grow(self):
        self.body.append((self.x, self.y))

    def move(self, move):
        """
        move:
        -1: left
        0: forward
        1: right
        """
        self.direction += move
        self.direction %= 4

        if self.direction == 0:
            self.x += self.size
        elif self.direction == 1:
            self.y += self.size
        elif self.direction == 2:
            self.x -= self.size
        elif self.direction == 3:
            self.y -= self.size

        self.body[0] = (self.x, self.y)

        for i in reversed(range(0, len(self.body))):
            if i != 0:
                self.body[i] = self.body[i - 1]

    def draw(self, win):
        pygame.draw.rect(win, red1, (self.x, self.y, self.size, self.size))
        for segment in self.body:
            pygame.draw.rect(win, red2, (segment[0], segment[1], self.size, self.size))


class Fruit:
    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.size = size
        self.generate()

    def generate(self):
        self.x = random.randint(0, (WIN_WIDTH-self.size)/self.size) * self.size
        self.y = random.randint(0, (WIN_HEIGHT-self.size)/self.size) * self.size

    def draw(self, win):
        pygame.draw.rect(win, green, (self.x, self.y, self.size, self.size))


def window_draw(win, snake, fruit):
    win.fill((50, 50, 50))

    snake.draw(win)
    fruit.draw(win)


def main(genomes=None, config=None):
    FPS = 10

    if genomes is None:
        snake = Snake(WIN_WIDTH // 2, WIN_HEIGHT // 2, 20)
        fruit = Fruit(20)
    else:
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

        if genomes is None:
            keys = pygame.key.get_pressed()
            move = 0
            if keys[pygame.K_a]:
                move = -1
            elif keys[pygame.K_d]:
                move = 1
            print(move)

        snake.move(move)
        if (fruit.x, fruit.y) == (snake.x, snake.y):
            fruit.generate()
            snake.grow()

        window_draw(win, snake, fruit)
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
