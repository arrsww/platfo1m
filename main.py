import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
from load import *


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):

            # столкновение ногами с блоком
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            # толкновение головой с блоком
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velosity_y = 0
            # столкновение правой стороной
            if abs(self.rect.left - player.rect.right) < 15 and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left

                # столкновение левой стороной с блоком
            if (abs(self.rect.right - player.rect.left) < 15 and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5


        self.velosity_y = 0
        self.on_ground = True



        self.dir = 'right'
        self.timer_attack = 0
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
        self.key = pygame.key.get_pressed()
        self.velocity_y = 15
    def jump(self):
        if self.key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10

    def attack(self):
        self.timer_attack += 1
        if self.key[pygame.K_e] and self.timer_attack / FPS > 1:
            fireball = Fireball(self.rect.center, self.dir)
            fireball_group.add(fireball)
            camera_group.add(fireball)
            self.timer_attack = 0
    def move(self):
        if self.key[pygame.K_d]:
            self.dir = 'right'
            self.anime = True
            self.image = player_image[self.frame]
            self.rect.x += self.speed
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        elif self.key[pygame.K_a]:
            self.anime = False
            self.dir = 'left'
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(player_image[self.frame], True, False)
            if self.rect.left < 100:
                self.rect.left = 100
                camera_group.update(self.speed)

        else:
            self.anime = False

    def animation(self):
        if self.anime:
            print(self.timer_anime)
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self):
        self.animation()
        self.move()
        self.jump()
        self.attack()
        self.key = pygame.key.get_pressed()




class Portal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Fireball(pygame.sprite.Sprite):
    def __init__(self, pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = fireball_image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1] - 20
        self.frame = 0
        self.anime = True
        self.timer_anime = 0
        if dir == 'left':
            self.speed = -5
        else:
            self.speed = 5


    def update(self, step):
        self.animation()
        self.rect.x +=  self.speed
        if self.speed < 0:
            self.image = fireball_image[self.frame]
        else:
            self.image = pygame.transform.flip(fireball_image[self.frame], True , False)


    def animation(self):
        if self.anime:
            self.timer_anime  += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(fireball_image) - 1:
                    self.kill()
                else:
                    self.frame += 1
                self.timer_anime = 0



class Monetka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class StopEnemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1

    def update(self, step):
        self.rect.x += step
        if self.dir == 1:
            self.rect.x += self.speed
        elif self.dir == -1:
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, stop_group, False):
            self.dir *= -1

        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def animation(self):
        if self.anime:
            print(self.timer_anime)
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

        if pygame.sprite.spritecollide(self, player_group, False):
            # столкновение ногами с блоком
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            # толкновение головой с блоком
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velosity_y = 0
            # столкновение правой стороной
            if abs(self.rect.left - player.rect.right) < 15 and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
                # столкновение левой стороной с блоком
            if (abs(self.rect.right - player.rect.left) < 15 and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


def restart():
    global player_group, earth_group, water_group, box_group, center_group, camera_group, stop_group , player , fireball_group
    player_group = pygame.sprite.Group()
    earth_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    player = Player(player_image, (400, 300))
    player_group.add(player)
    camera_group = pygame.sprite.Group()
    fireball_group = pygame.sprite.Group()


def game_lvl():
    sc.fill('black')
    player_group.update()
    player_group.draw(sc)
    earth_group.update(0)
    earth_group.draw(sc)
    water_group.update(0)
    water_group.draw(sc)
    box_group.update(0)
    box_group.draw(sc)
    center_group.update(0)
    center_group.draw(sc)
    fireball_group.update(0)
    fireball_group.draw(sc)
    pygame.display.update()




def drawMaps(nameFile):
    maps = []
    source = "game_lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == "1":
                box = Box(box_image, pos)
                box_group.add(box)
                camera_group.add(box)
            elif maps[i][j] == "2":
                center = Center(center_image, pos)
                center_group.add(center)
                camera_group.add(center)
            elif maps[i][j] == "3":
                earth = Earth(earth_image, pos)
                earth_group.add(earth)
                camera_group.add(earth)
            elif maps[i][j] == "4":
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)
            elif maps[i][j] == "4":
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)











restart()
drawMaps('1.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
