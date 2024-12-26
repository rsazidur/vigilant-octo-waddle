from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
ROBOT_ARM_WIDTH = 20
ROBOT_ARM_HEIGHT = 10
DEBRIS_SIZE = 10
TREASURE_SIZE = 15
SHRINKING_TREASURE_SIZE = 10
HEART_SIZE = 5

# Game variables
score = 0
lives = 6
robot_arm_x, robot_arm_y = SCREEN_WIDTH / 2, 100
robot_arm_dx, robot_arm_dy = 0, 0
treasures = []
debris = []
paused = False

# Functions
def drawpoints(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_circle(r, cx=0, cy=0):
    d = 1 - r
    x = 0
    y = r
    while x <= y:
        eight_way_symmetry(x, y, cx, cy)
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1

def eight_way_symmetry(x, y, cx, cy):
    drawpoints(cx + x, cy + y)
    drawpoints(cx - x, cy + y)
    drawpoints(cx + x, cy - y)
    drawpoints(cx - x, cy - y)
    drawpoints(cx + y, cy + x)
    drawpoints(cx - y, cy + x)
    drawpoints(cx + y, cy - x)
    drawpoints(cx - y, cy - x)

def initialize_entities():
    global treasures, debris
    treasures = [[random.randint(0, SCREEN_WIDTH), random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200), random.choice([TREASURE_SIZE, SHRINKING_TREASURE_SIZE])] for _ in range(10)]
    debris = [[random.randint(0, SCREEN_WIDTH), random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200), DEBRIS_SIZE] for _ in range(5)]

def draw_robot_arm():
    glBegin(GL_QUADS)
    glVertex2f(robot_arm_x - ROBOT_ARM_WIDTH / 2, robot_arm_y)
    glVertex2f(robot_arm_x + ROBOT_ARM_WIDTH / 2, robot_arm_y)
    glVertex2f(robot_arm_x + ROBOT_ARM_WIDTH / 2, robot_arm_y + ROBOT_ARM_HEIGHT)
    glVertex2f(robot_arm_x - ROBOT_ARM_WIDTH / 2, robot_arm_y + ROBOT_ARM_HEIGHT)
    glEnd()

def draw_treasures():
    for treasure in treasures:
        draw_circle(treasure[2], treasure[0], treasure[1])

def draw_debris():
    for d in debris:
        draw_circle(d[2], d[0], d[1])

def move_robot_arm():
    global robot_arm_x, robot_arm_y
    if not paused:
        robot_arm_x += robot_arm_dx
        robot_arm_y += robot_arm_dy
        robot_arm_x = max(0, min(SCREEN_WIDTH, robot_arm_x))
        robot_arm_y = max(0, min(SCREEN_HEIGHT, robot_arm_y))

def detect_collisions():
    global score, lives
    treasures[:] = [t for t in treasures if not (robot_arm_x - ROBOT_ARM_WIDTH / 2 <= t[0] <= robot_arm_x + ROBOT_ARM_WIDTH / 2 and robot_arm_y <= t[1] <= robot_arm_y + ROBOT_ARM_HEIGHT)]
    debris[:] = [d for d in debris if not (robot_arm_x - ROBOT_ARM_WIDTH / 2 <= d[0] <= robot_arm_x + ROBOT_ARM_WIDTH / 2 and robot_arm_y <= d[1] <= robot_arm_y + ROBOT_ARM_HEIGHT)]

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_robot_arm()
    draw_treasures()
    draw_debris()
    detect_collisions()
    move_robot_arm()
    glutSwapBuffers()

def keyboard(key, x, y):
    global robot_arm_dx, robot_arm_dy, paused
    if key == b'\x1b':
        sys.exit()
    elif key == b' ':
        paused = not paused

def special_keys(key, x, y):
    global robot_arm_dx, robot_arm_dy
    if key == GLUT_KEY_LEFT:
        robot_arm_dx = -5
    elif key == GLUT_KEY_RIGHT:
        robot_arm_dx = 5
    elif key == GLUT_KEY_UP:
        robot_arm_dy = 5
    elif key == GLUT_KEY_DOWN:
        robot_arm_dy = -5

def special_keys_up(key, x, y):
    global robot_arm_dx, robot_arm_dy
    if key in (GLUT_KEY_LEFT, GLUT_KEY_RIGHT):
        robot_arm_dx = 0
    elif key in (GLUT_KEY_UP, GLUT_KEY_DOWN):
        robot_arm_dy = 0

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutCreateWindow(b"Space Probe Game")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
    initialize_entities()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutSpecialUpFunc(special_keys_up)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()