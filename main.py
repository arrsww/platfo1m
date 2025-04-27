import pygame
import os
import sys
import random

from Tools.demo.spreadsheet import center

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
from load import *



class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos ):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos ):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos ):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos ):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos ):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)

        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left < 100:
                self.rect.left = 100
                camera_group.update(self.speed)




def restart():
    global player_group, earth_group, water_group, box_group, center_group,camera_group
    player_group = pygame.sprite.Group()
    earth_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    player = Player(player_image,(300, 300))
    player_group.add(player)
    camera_group = pygame.sprite.Group()


def drawMaps(nameFile):
    maps = []
    source = "game_lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("/n", "").split(",")[0:-1])
    pos = [0,0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0,len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == "1":
                box = Box(box_image, pos)
                box_group.add(box)
                camera_group.add(box)
            if maps[i][j] == "2":
                center = Center(center_image, pos)
                center_group.add(center)
                camera_group.add(center)
            if maps[i][j] == "3":
                earth = Earth(earth_image, pos)
                earth_group.add(earth)
                camera_group.add(earth)
            if maps[i][j] == "4":
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)

def game_lvl():
    sc.fill('grey')

    earth_group.update(0)
    earth_group.draw(sc)
    water_group.update(0)
    water_group.draw(sc)
    box_group.draw(sc)
    center_group.update(0)
    center_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    pygame.display.update()










restart()
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
