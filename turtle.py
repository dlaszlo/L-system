import math


class Turtle:

    def __init__(self, width: int, height: int, x: int = None, y: int = None, orientation: int = 180):
        self.width = width
        self.height = height
        self.x = float(width / 2 if x is None else x)
        self.y = float(height if y is None else y)
        self.orientation = float(orientation)
        self.image = [[0 for i in range(width)] for j in range(height)]
        self.pen = True
        self.state = []

    def pen_up(self):
        self.pen = False

    def pen_down(self):
        self.pen = True

    def plot(self, x, y):
        x0 = round(x)
        y0 = round(y)
        if self.pen and 0 <= x0 < self.width and 0 <= y0 < self.height:
            self.image[y0][x0] = 1

    def push(self):
        self.state.append((self.x, self.y, self.orientation, self.pen))

    def pop(self):
        (self.x, self.y, self.orientation, self.pen) = self.state.pop()

    def rotate(self, o):
        self.orientation = self.orientation + o

    def goto(self, x, y):
        self.x = x
        self.y = y

    def set_orientation(self, orientation):
        self.orientation = orientation

    def get_orientation(self):
        return self.orientation

    def get_position(self):
        return self.x, self.y

    def get_pen(self):
        return self.pen

    def draw(self, length):
        x1 = self.x
        y1 = self.y
        x2 = x1 + (math.sin(self.orientation * math.pi / 180) * length)
        y2 = y1 + (math.cos(self.orientation * math.pi / 180) * length)

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        if dy > dx:
            sy = 1 if y1 < y2 else -1
            sx = dx / dy if x1 < x2 else -dx / dy
            for i in range(round(dy)):
                self.plot(x1, y1)
                self.x = x1
                self.y = y1
                x1 = x1 + sx
                y1 = y1 + sy
        else:
            sx = 1 if x1 < x2 else -1
            sy = dy / dx if y1 < y2 else -dy / dx
            for i in range(round(dx)):
                self.plot(x1, y1)
                self.x = x1
                self.y = y1
                x1 = x1 + sx
                y1 = y1 + sy

        self.x = x2
        self.y = y2

    def get_image(self):
        return self.image
