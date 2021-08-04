import pygame

WIDTH = 700  # ширина игрового окна
HEIGHT = 700  # высота игрового окна
FPS = 30  # частота кадров в секунду

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
lines = []


def _add_end_point(x, y):
    _, (p2_x, p2_y) = lines[-1]
    lines.append([[p2_x, p2_y], [p2_x + x, p2_y + y]])


def _add_polar_line(leangh, grad):
    _dict = {0: (leangh, 0),
             90: (0, -leangh),
             180: (-leangh, 0),
             270: (0, leangh)}
    x, y = _dict[grad % 360]
    _add_end_point(x, y)


def base1(deep, leangh=30, angle = 0):
    """ start____
                |
            ____|
    """
    if deep <= 0:
        return
    deep -= 1

    base2(deep, leangh, angle=0)
    angle += 0
    _add_polar_line(leangh, angle)

    base1(deep, leangh, angle=0)
    angle += 270
    _add_polar_line(leangh, angle)

    base1(deep, leangh, angle=0)
    angle += 270
    _add_polar_line(leangh, angle)

    base4(deep, leangh, angle=0)


def base2(deep, leangh=30, angle = 0):
    """ start|    |
             |____|
     """
    if deep <= 0:
        return
    deep -= 1

    base1(deep, leangh, angle=0)
    angle += 270
    _add_polar_line(leangh, angle)

    base2(deep, leangh, angle=0)
    angle += 90
    _add_polar_line(leangh, angle)

    base2(deep, leangh, angle=0)
    angle += 90
    _add_polar_line(leangh, angle)

    base3(deep, leangh, angle=0)


def base3(deep, leangh=30, angle = 0):
    """
    _____
    |
    |____start
    """
    if deep <= 0:
        return
    deep -= 1

    base4(deep, leangh, angle=0)
    angle += 180
    _add_polar_line(leangh, angle)

    base3(deep, leangh, angle=0)
    angle += 270
    _add_polar_line(leangh, angle)

    base3(deep, leangh, angle=0)
    angle += 270
    _add_polar_line(leangh, angle)

    base2(deep, leangh, angle=0)


def base4(deep, leangh=30, angle = 0):
    """
    ______
    |    |
    |    |start
    """
    if deep <= 0:
        return
    deep -= 1

    base3(deep, leangh, angle=0)
    angle += 90
    _add_polar_line(leangh, angle)

    base4(deep, leangh, angle=0)
    angle += 90
    _add_polar_line(leangh, angle)

    base4(deep, leangh, angle=0)
    angle += 90
    _add_polar_line(leangh, angle)

    base1(deep, leangh, angle=0)


lines = [[[10, 10], [10, 10]]]
base1(5, 20)
screen.fill((0, 0, 0))
[pygame.draw.aaline(screen, (255, 255, 255),
                    point1,
                    point2) for (point1, point2) in lines]

while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(FPS)
