import numpy as np
from math import *

gr = (1 + sqrt(5)) / 2 # golden ratio

# these are some shapes that i have created
# they are stored in matrixes of 3 dimensional
# vertices as cartesian coordinates
# you can add your own, and to render
# your shape, change the 'shape'
# variable in the code_.py file
# to your shape you have created

# https://en.wikipedia.org/wiki/Cartesian_coordinate_system

cube = [
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1]
]

tetrahedron = [
    [ 1,  1,  1],
    [ 1, -1, -1],
    [-1,  1, -1],
    [-1, -1,  1]
]

octahedron = [
    [-1,  0,  0],
    [ 1,  0,  0],
    [ 0, -1,  0],
    [ 0,  1,  0],
    [ 0,  0, -1],
    [ 0,  0,  1]
]

isosahedron = [
    [  0, -1, -gr],
    [  0, -1,  gr],
    [  0,  1, -gr],
    [  0,  1,  gr],
    [ -1, -gr, 0],
    [ -1,  gr, 0],
    [  1, -gr, 0],
    [  1,  gr, 0],
    [-gr,  0, -1],
    [-gr,  0,  1],
    [ gr,  0, -1],
    [ gr,  0,  1]
]

dodecahedron = [
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],

    [0, -1/gr,  gr],
    [0, -1/gr,  gr],
    [0,  1/gr,  gr],
    [0,  1/gr,  gr],
    [0, -1/gr, -gr],
    [0, -1/gr, -gr],
    [0,  1/gr, -gr],
    [0,  1/gr, -gr],

    [-1/gr, -gr,  0],
    [ 1/gr, -gr,  0],
    [ 1/gr,  gr,  0],
    [-1/gr,  gr,  0],
    [-1/gr, -gr,  0],
    [ 1/gr, -gr,  0],
    [ 1/gr,  gr,  0],
    [-1/gr,  gr,  0],

    [-gr,  0,  1/gr],
    [ gr,  0,  1/gr],
    [ gr,  0,  1/gr],
    [-gr,  0,  1/gr],
    [-gr,  0, -1/gr],
    [ gr,  0, -1/gr],
    [ gr,  0, -1/gr],
    [-gr,  0, -1/gr]
]