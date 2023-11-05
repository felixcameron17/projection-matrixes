import shapes
import pygame as pg
import numpy as np
from math import *

# constant variables
WIDTH, HEIGHT = 800, 600
SCALE = 100
CIRCLE_POS = [WIDTH/2, HEIGHT/2]

# shape selector
shape = shapes.dodecahedron

# other variables
angle = 0
points = []


# convert each vertice into a numpy matrix
for vertice in shape:
    points.append(np.matrix(vertice))


# projection matrix. this is a constant variable
PROJECTION_MATRIX = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
#   [0, 0, 0] but its not needed to compute as it is all zeroes
])

# initialize list for x, y cords to display on screen
projected_points = [
    [n, n] for n in range(len(points))
]

# pygame variables
pg.display.set_caption('3D projection')
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
running = True

# game loop
while running:

    # check if 'game' ended
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()


    rot_x = np.matrix([ # rotation matrix for x axis
        [1,          0,           0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle),  cos(angle)]
    ])

    rot_y = np.matrix([ # rotation matrix for y axis
        [cos(angle),  0, sin(angle)],
        [0,           1,          0],
        [-sin(angle), 0, cos(angle)]
    ])

    rot_z = np.matrix([ # rotation matrix for z axis
        [cos(angle), -sin(angle), 0],
        [sin(angle),  cos(angle), 0],
        [         0,           0, 1]
    ])

    # variables
    angle += 0.01
    screen.fill((225, 255, 245))

    # applying matrix multiplication
    for i, point in enumerate(points):
        rotated2d   = np.dot(rot_x, point.reshape((3, 1))) # x matrix multiplication
        rotated2d   = np.dot(rot_y, rotated2d)             # y matrix multiplication
        rotated2d   = np.dot(rot_z, rotated2d)             # z matrix multiplication
        projected2d = np.dot(PROJECTION_MATRIX, rotated2d)
        x = int(projected2d[0][0] * SCALE) + CIRCLE_POS[0]
        y = int(projected2d[1][0] * SCALE) + CIRCLE_POS[1]

        projected_points[i] = [x, y] # update projected poins list with x, y cords
        pg.draw.circle(screen, 'BLACK', (x, y), 5) # draw points


    pg.display.update()