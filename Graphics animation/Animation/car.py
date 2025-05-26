import pygame # type: ignore
import sys
import math

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Animation")

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
DARK_GRAY = (50, 50, 50)
LIGHT_YELLOW = (255, 255, 153)

car_x = 0
car_y = 250
car_speed = 2

bird_positions = [[100, 50], [200, 70], [300, 60]]
bird_speed = 1

clock = pygame.time.Clock()

def draw_car(x, y):
    # Body
    pygame.draw.rect(screen, RED, (x, y, 100, 40), border_radius=10)
    # Roof
    pygame.draw.polygon(screen, GRAY, [(x+20, y), (x+40, y-20), (x+60, y-20), (x+80, y)])
    # Windows
    pygame.draw.polygon(screen, WHITE, [(x+42, y-18), (x+58, y-18), (x+58, y), (x+42, y)])
    # Wheels
    pygame.draw.circle(screen, BLACK, (x + 25, y + 40), 12)
    pygame.draw.circle(screen, BLACK, (x + 75, y + 40), 12)

def draw_road():
    pygame.draw.rect(screen, DARK_GRAY, (0, 290, width, 110))
    for i in range(0, width, 40):
        pygame.draw.rect(screen, WHITE, (i, 340, 20, 5))

def draw_sun():
    pygame.draw.circle(screen, YELLOW, (700, 80), 40)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = 700 + int(50 * math.cos(rad))
        y1 = 80 + int(50 * math.sin(rad))
        x2 = 700 + int(70 * math.cos(rad))
        y2 = 80 + int(70 * math.sin(rad))
        pygame.draw.line(screen, LIGHT_YELLOW, (x1, y1), (x2, y2), 2)

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, (x + 15, y + 60, 20, 40))
    pygame.draw.circle(screen, GREEN, (x + 25, y + 50), 25)
    pygame.draw.circle(screen, GREEN, (x + 10, y + 40), 20)
    pygame.draw.circle(screen, GREEN, (x + 40, y + 40), 20)

def draw_bird(x, y):
    pygame.draw.arc(screen, BLACK, [x, y, 20, 10], math.pi, 2 * math.pi, 2)
    pygame.draw.arc(screen, BLACK, [x + 20, y, 20, 10], math.pi, 2 * math.pi, 2)

while True:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_sun()
    draw_tree(100, 200)
    draw_tree(220, 210)
    draw_tree(650, 220)

    for bird in bird_positions:
        draw_bird(bird[0], bird[1])
        bird[0] += bird_speed
        if bird[0] > width:
            bird[0] = -40

    draw_road()
    draw_car(car_x, car_y)
    car_x += car_speed
    if car_x > width:
        car_x = -100

    pygame.display.update()
    clock.tick(60)