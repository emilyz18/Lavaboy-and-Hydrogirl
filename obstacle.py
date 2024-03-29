import pygame
from character import *

tile_size = 34


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, type, screen):
        type.draw(screen)


class Lava(Obstacle):
    def __init__(self, x, y):
        self.lava_image = pygame.image.load("img/lava.png")
        self.image = pygame.transform.scale(self.lava_image, (tile_size, tile_size - 8))
        super().__init__(x, y)


class Water(Obstacle):
    def __init__(self, x, y):
        self.water_image = pygame.image.load("img/water.png")
        self.image = pygame.transform.scale(self.water_image, (tile_size, tile_size - 8))
        super().__init__(x, y)
        self.top_collision = False


class Slime(Obstacle):
    def __init__(self, x, y):
        self.slime_image = pygame.image.load("img/slime.png")
        self.image = pygame.transform.scale(self.slime_image, (tile_size, tile_size - 8))
        super().__init__(x, y)


class Speeder(Obstacle):
    def __init__(self, x, y, fb, wg, direction):
        image = pygame.image.load("img/speeder.png")
        if direction == "right":
            self.speeder_image = image
        else:
            self.speeder_image = pygame.transform.flip(image, True, False)
            # pygame.transform.flip(img_right, True, False)

        self.image = pygame.transform.scale(self.speeder_image, (34, 18))
        self.top_collision = False
        self.fb = fb
        self.wg = wg
        self.direction = direction
        super().__init__(x, y)

    def turn_on(self, c_type):
        self.top_collision = False

        if c_type == "fb":
            c_rect = self.fb.rt_rect()
            c_img = self.fb.rt_img()
            c_momentum = self.fb.rt_momentum()

            c_rect_x = c_rect.x
            c_dx = Character.fb_dx
            c_dy = Character.fb_dy
            c_rect_y = c_rect.y
        if c_type == "wg":
            c_rect = self.wg.rt_rect()
            c_img = self.wg.rt_img()
            c_momentum = self.wg.rt_momentum()

            c_rect_x = c_rect.x
            c_dx = Character.wg_dx
            c_dy = Character.wg_dy
            c_rect_y = c_rect.y

        if self.rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):
            if c_type == "fb":
                Character.fb_dx = 0
            if c_type == "wg":
                Character.wg_dx = 0

        if self.rect.colliderect(c_rect_x, c_rect_y + c_dy, c_img.get_width(), c_img.get_height()):
            if c_momentum < 0:
                if c_type == "fb":
                    Character.fb_dy = self.rect.bottom - c_rect.top
                if c_type == "wg":
                    Character.wg_dy = self.rect.bottom - c_rect.top


            elif c_momentum >= 0:  # touch from top
                self.top_collision = True
                # print(self.top_collision)

                c_rect.bottom = self.rect.top - c_dy
                if self.direction == "right":
                    if c_type == "fb":
                        Character.fb_dx += 2
                    if c_type == "wg":
                        Character.wg_dx += 2
                else:
                    if c_type == "fb":
                        Character.fb_dx -= 2
                    if c_type == "wg":
                        Character.wg_dx -= 2

        return self.top_collision


class Coin(Obstacle):
    def __init__(self, x, y):
        image = pygame.image.load("img/coin.png")
        self.image = pygame.transform.scale(image, (tile_size - 12, tile_size - 12))
        super().__init__(x, y)
        self.rect.center = (x + 17,y + 17)



class RedGem(Obstacle):
    def __init__(self, x, y):
        image = pygame.image.load("img/redGem.png")
        self.image = pygame.transform.scale(image, (tile_size - 12, tile_size - 16))
        super().__init__(x, y)


class BlueGem(Obstacle):
    def __init__(self, x, y):
        image = pygame.image.load("img/blueGem.png")
        self.image = pygame.transform.scale(image, (tile_size - 12, tile_size - 16))
        super().__init__(x, y)


class FbDoor(Obstacle):
    def __init__(self, x, y):
        self.image = pygame.image.load("img/fbDoor.png")
        # self.image = pygame.transform.scale(image, (tile_size -, tile_size - 16))
        super().__init__(x, y - 6)

class WgDoor(Obstacle):
    def __init__(self, x, y):
        self.image = pygame.image.load("img/wgDoor.png")
        # self.image = pygame.transform.scale(image, (tile_size -, tile_size - 16))
        super().__init__(x, y - 6)