import pygame

from turtle import Turtle


class Screen:

    def __init__(self, turtle: Turtle, width: int, height: int):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.run = True
        self.turtle = turtle

    def check_quit(self):
        if self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
            if not self.run:
                pygame.quit()

        return self.run

    def delay(self, delay):
        if self.run:
            pygame.time.delay(delay)

    def update(self):
        if self.run:
            image = self.turtle.get_image()
            dx = self.width / float(len(image[0]))
            dy = self.height / float(len(image))

            self.screen.fill((0, 0, 0))

            for x in range(len(image[0])):
                for y in range(len(image)):
                    if image[y][x] == 1:
                        pygame.draw.rect(self.screen, (255, 255, 255),
                                         pygame.Rect(int(dx * x), int(dy * y), int(dx), int(dy))
                                         )

            pygame.display.update()
