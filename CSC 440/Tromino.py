import turtle
import math
import random
import time


def fill_up(x, y, s, p):
    """
    :param x: the furthest x coordinate of the square
    :param y: the furthest y coordinate of the square
    :param s: the size of the square
    :param p: the x, y coordinate of the 1x1 missing square
    :return:
    """
    global count, matrix

    if s == 2:  # base case: the  2 x 2 square
        count += 1
        original = matrix[p[0]][p[1]]
        matrix[x][y], matrix[x - 1][y - 1] = count, count
        matrix[x - 1][y], matrix[x][y - 1] = count, count
        matrix[p[0]][p[1]] = original
        return

    s_new = s // 2
    x1, y1, x2, y2, x3, y3 = x - s_new, y - s_new, x, y - s_new, x - s_new, y
    p1 = p if x1 >= p[0] > x1 - s_new and y1 >= p[1] > y1 - s_new else (x1, y1)
    p2 = p if x2 >= p[0] > x2 - s_new and y2 >= p[1] > y2 - s_new else (x1 + 1, y1)
    p3 = p if x3 >= p[0] > x3 - s_new and y3 >= p[1] > y3 - s_new else (x1, y1 + 1)
    p4 = p if x >= p[0] > x - s_new and y >= p[1] > y - s_new else (x1 + 1, y1 + 1)
    for i in [p1, p2, p3, p4]:
        if matrix[i[0]][i[1]] == 0:
            matrix[i[0]][i[1]] = count
    count += 1
    fill_up(x1, y1, s_new, p1)  # 1st quadrant
    fill_up(x2, y2, s_new, p2)  # 2nd quadrant
    fill_up(x3, y3, s_new, p3)  # 3rd quadrant
    fill_up(x, y, s_new, p4)  # 4th quadrant


def draw_square(matrix, n):
    # draw it in turtle
    wn = turtle.Screen()
    k = turtle.Turtle()
    k.speed(0)
    k.penup()
    k.resizemode("user")
    k.shape('square')
    k.shapesize((560 / n)*(1/26), (560 / n) * (1/26), outline=None)
    for i in range(n + 1):
        k.goto((-325, 260 - (i * (560 / n))))
        k.pendown()
        k.forward(560)
        k.penup()
        k.goto((-325 + (i * (560 / n)), 260))
        k.pendown()
        k.right(90)
        k.forward(560)
        k.penup()
        k.left(90)
    while True:

        colors = {}
        for j, columns in enumerate(matrix):
            for i, cols in enumerate(columns):
                if cols != 'x':
                    k.goto((280 / n) + -325 + (i * (560 / n)), 260 - (280 / n) - (j * (560 / n)))
                    if cols in colors:
                        k.color(colors[cols])
                        k.stamp()
                    else:
                        colors[cols] = random.choice(['white', 'yellow', 'gold', 'orange', 'red', 'crimson','Rosy Brown', 'Tomato', 'Thistle',
                                                       'maroon', 'violet', 'magenta', 'purple', 'darkolivegreen', 'Plum',
                                                       'navy', 'Pale Goldenrod', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green',
                                                       'darkgreen', 'chocolate', 'brown', 'gray', 'black'])
                        k.color(colors[cols])
                        k.stamp()


if __name__ == "__main__":
    count = 1
    n = int(input("Please type the integer n for 2^n square matrix: "))
    x = int(input("Please input the desired x coordinate of the missing 1 x 1 square. (x <= 2^n): ")) % 2**n
    y = int(input("Please input the desired y coordinate of the missing 1 x 1 square.(y <= 2^n): ")) % 2**n
    a = time.process_time()
    matrix = [[0] * 2**n for i in range(2**n)]
    matrix[x - 1][y - 1] = 'x'
    fill_up(2**n-1, 2**n-1, 2**n, (x-1, y-1))
    b = time.process_time()
    for i in matrix:
        print(i)
    print(b-a)
    draw_square(matrix, 2**n)
