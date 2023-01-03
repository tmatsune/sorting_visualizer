import pygame
import random
import time

WIDTH = 1000
HEIGHT = 600
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
GREEN = (0,255,0)
RED = (255, 0, 0)
BLACK = (0,0,0)

colors = []
min_bar = 20
max_bar = 500
bar_width = 20
pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('sorting')
font = pygame.font.SysFont('freesansbold.tff', 40)

def insertion_sort(lis):
    for i in range(1, len(lis)):
        j = i
        while lis[j - 1] > lis[j] and j > 0:
            draw(WINDOW, lis, bar_width, j - 1, j, True)
            lis[j - 1], lis[j] = lis[j], lis[j-1]
            j -= 1
    print(lis)
    return lis


def bubble_sort(lis, ascending=True):
    n = len(lis)
    for i in range(n):

        swapped = False
        for j in range(n-i-1):
            if (lis[j] > lis[j+1] and ascending) or lis[j] < lis[j+1] and not ascending:
                lis[j], lis[j+1] = lis[j+1], lis[j]
                swapped = True
                # allows you to use other elements on keyboard
            draw(WINDOW, lis, bar_width, j, j+1,True)
            #draw_bars(lis, WINDOW, bar_width)

        if swapped == False:
            break
    print(lis)
    return lis

def partition(lis, left, right):
    i = left
    j = right - 1
    pivot = lis[right]
    while i < j:
        while i < right and lis[i] < pivot:
            draw(WINDOW, lis, bar_width, i, j, True)
            time.sleep(0.04)
            i += 1
        while j > left and lis[j] >= pivot:
            draw(WINDOW, lis, bar_width, j, i, True)
            time.sleep(0.04)
            j -= 1
        if i < j:
            lis[i], lis[j] = lis[j], lis[i]
            #draw(WINDOW, lis, bar_width, j, i,True)
            #time.sleep(0.14)
    if lis[i] > pivot:
        lis[i], lis[right] = lis[right], lis[i]
    return i, lis

def quick_sort(lis, left, right):
    if left < right:
        partition_position = partition(lis, left, right)
        quick_sort(lis, left, partition_position[0] - 1)
        quick_sort(lis, partition_position[0] + 1, right)
        return partition_position[1]

def bar_values(min_value, max_value, amount):
    lis = []
    for i in range(amount):
        val = random.randrange(min_value, max_value)
        lis.append(val)
    print(lis)
    return lis

def draw_bars(lis, window, bar_width, num,num2,item=False):
    for i, j in enumerate(lis):
        x = i * 22 + 50
        y = 600 - j
        color = PURPLE
        if item == True and i == num:
            color = RED
        if item == True and i == num2:
            color = GREEN
        if item == 'DONE':
            color = GREEN
        pygame.draw.rect(window, color, (x, y, bar_width, j))
        # have to update this to animate visulaization
    pygame.display.update()
# i * 15 + 10
# bar_width = 10

def draw(window, lis, bar_width, num,num2,TorF):
    window.fill(WHITE)
    angle = font.render("Press 'B' for Bubble Sort:          Press 'Q' for Quick sort:", 1, BLACK)
    window.blit(angle, (110, 30))
    angle = font.render("Press 'I' for Insertion Sort:          Press 'R' to reset:", 1, BLACK)
    window.blit(angle, (110, 60))
    draw_bars(lis, window, bar_width, num,num2,TorF)
    pygame.display.update()

def main(window):

    amount = bar_values(min_bar, max_bar, 40)
    clock = pygame.time.Clock()
    ascending = True
    run = True
    while run:
        clock.tick(60)
        draw(window, amount, bar_width, 0,0,False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    ascending = False
                    print(ascending)
                if event.key == pygame.K_a:
                    ascending = True
                if event.key == pygame.K_b:
                    new = bubble_sort(amount, ascending)
                    for i in range(len(amount)):
                        draw(WINDOW, amount, bar_width, i, i, True)
                if event.key == pygame.K_q:
                    new = quick_sort(amount, 0, len(amount)-1)
                    for i in range(len(amount)):
                        draw(WINDOW, amount, bar_width, i, i, True)

                if event.key == pygame.K_i:
                    new = insertion_sort(amount)
                    for i in range(len(amount)):
                        draw(WINDOW, amount, bar_width, i, i, True)
                if event.key == pygame.K_r:
                    amount = bar_values(min_bar, max_bar, 40)


    pygame.quit()

main(WINDOW)
