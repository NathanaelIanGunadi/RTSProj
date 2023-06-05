import pygame as pg


class Sprite(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)

        self.gameObj = game

        self.spriteType = ["tile", "entity", "background", "hpBar", "text", "button", "window", "map", "talkbox"]
        self.spriteList = {}

        for spriteType in self.spriteType:
            self.spriteList[spriteType] = []

        self.prio_sprites = []

        self.surface = self.gameObj.window.screen

    def newSprite(self, name, img, pos, type, prio, state, id, col_box_size=None, col_box_pos=None, size=None):
        self.spriteObj = NewSprite(self, name, img, pos, type, prio, state, id, col_box_size, col_box_pos, size)

        self.check_prio(prio)

        return self.spriteObj

    def check_prio(self, prio):
        check_prio = True
        while check_prio:
            if self.prio_sprites == []:
                self.prio_sprites.append(self.spriteObj.priority)
                check_prio = False
            elif prio not in self.prio_sprites:
                if self.prio_sprites[-1] + 1 != prio:
                    self.prio_sprites.append(self.prio_sprites[-1] + 1)
                else:
                    self.prio_sprites.append(self.spriteObj.priority)
                    check_prio = False
            else:
                check_prio = False

        self.prio_sprites.sort()


    def update(self, gameObj):
        self.gameObj = gameObj
        for spriteLists in self.spriteList:
            for sprites in self.spriteList[spriteLists]:
                for prio in self.prio_sprites:
                    if sprites.spriteObj.priority == prio:
                        sprites.update(self.gameObj)

class NewSprite(pg.sprite.Sprite):

    def __init__(self, spriteClass, name, img, pos, spr_type, prio, state, id, col_box_size=None, col_box_pos=None, size=None):
        self.spriteList = []
        self.spriteClass = spriteClass

        self.org_pos = pos
        self.pos = pos
        self.posX, self.posY = pos[0], pos[1]
        self.camera_pos_reseter = (0, 0)

        if spr_type in spriteClass.spriteType:
            self.type = spr_type

        self.name = name

        if type(img) == type(pg.Surface((0, 0))):
            self.img = img
        else:
            self.img = self.import_image(img)


        self.origine_img = self.img
        self.state = state

        self.spr_id = "#" + str(len(self.spriteClass.spriteList))
        self.id = id

        self.rect = self.img.get_rect()
        self.rect.topleft = (self.posX, self.posY)

        if size == None:
            self.size = self.get_sprite_size()
        else:
            self.size = size

        self.org_prio = prio
        self.priority = prio

        self.colision_box_size = (0, 0)
        self.colision_box_pos = (0, 0)

        self.isNotMoveble = False
        self.isMoving = False

        if col_box_size != None and col_box_pos != None:

            self.is_colision, self.col_state = True, True

            self.show_col = False

            self.colision_box_size = col_box_size
            self.colision_box_pos = col_box_pos

            if not self.colision_box_size < self.size:
                if self.colision_box_pos[0] > 0 and self.colision_box_pos[1] > 0 or self.colision_box_pos[0] >= 0 and self.colision_box_pos[1] > 0 or self.colision_box_pos[0] > 0 and self.colision_box_pos[1] >= 0:
                    self.new_size = ((self.colision_box_size[0] + self.size[0]) - (self.size[0] - self.colision_box_pos[0]), (self.colision_box_size[1] + self.size[1]) - (self.size[1] - self.colision_box_pos[1]))
                    self.new_img = pg.Surface(self.new_size)

            if self.colision_box_pos[0] < 0 and self.colision_box_pos[1] >= 0:
                self.new_size = ((self.colision_box_size[0] + self.size[0]) - self.colision_box_pos[0], (self.colision_box_size[1] + self.size[1]) - self.colision_box_pos[1])
                self.new_img = pg.Surface(self.new_size)

            if self.colision_box_pos[0] >= 0 and self.colision_box_pos[1] < 0:
                self.new_size = ((self.colision_box_size[0] + self.size[0]) - (self.size[0] - self.colision_box_pos[0]), (self.colision_box_size[1] + self.size[1]) - (self.size[1] - self.colision_box_pos[1]))
                self.new_img = pg.Surface(self.new_size)

            if self.colision_box_pos[0] < 0 and self.colision_box_pos[1] < 0:
                self.new_size = ((self.colision_box_size[0] + self.size[0]) - (self.size[0] - self.colision_box_pos[0]), (self.colision_box_size[1] + self.size[1]) - (self.size[1] - self.colision_box_pos[1]))
                self.new_img = pg.Surface(self.new_size)

            self.empty_col_box = pg.Color(0,0,0,0)
            self.colision_box = pg.Surface(self.colision_box_size, flags=pg.SRCALPHA)

            self.colision_box.convert_alpha()

        else:
            self.is_colision, self.col_state = False, False

        self.spriteList.append(self)

    def sprite_coll_with(self, direction, speed):

        self.spr_col_rect = pg.Rect(self.posX, self.posY, self.colision_box_size[0], self.colision_box_size[1])

        for all_sprite in self.spriteClass.spriteList:
            self.all_spr_col_rect = pg.Rect(all_sprite.posX, all_sprite.posY, all_sprite.colision_box_size[0], all_sprite.colision_box_size[1])

            self.spr_col_rect = pg.Rect(self.posX - speed, self.posY, self.colision_box_size[0], self.colision_box_size[1])
            if all_sprite.col_state and pg.Rect.colliderect(self.spr_col_rect, self.all_spr_col_rect) and all_sprite.spr_id != self.spr_id:
                if self.spr_col_rect[0] >= self.all_spr_col_rect[0] and direction[0] < 0:
                    return True

            self.spr_col_rect = pg.Rect(self.posX + speed, self.posY, self.colision_box_size[0], self.colision_box_size[1])
            if all_sprite.col_state and pg.Rect.colliderect(self.spr_col_rect, self.all_spr_col_rect) and all_sprite.spr_id != self.spr_id:
                if self.spr_col_rect[0] <= self.all_spr_col_rect[0] and direction[0] > 0:
                    return True

            self.spr_col_rect = pg.Rect(self.posX, self.posY - speed, self.colision_box_size[0], self.colision_box_size[1])
            if all_sprite.col_state and pg.Rect.colliderect(self.spr_col_rect, self.all_spr_col_rect) and all_sprite.spr_id != self.spr_id:
                if self.spr_col_rect[1] >= self.all_spr_col_rect[1] and direction[1] < 0:
                    return True

            self.spr_col_rect = pg.Rect(self.posX, self.posY + speed, self.colision_box_size[0], self.colision_box_size[1])
            if all_sprite.col_state and pg.Rect.colliderect(self.spr_col_rect, self.all_spr_col_rect) and all_sprite.spr_id != self.spr_id:
                if self.spr_col_rect[1] <= self.all_spr_col_rect[1] and direction[1] > 0:
                    return True



        return False


    def update(self, gameObj):

        self.camera_pos = gameObj.world.camera.camera_pos
        if self.isNotMoveble == False and not gameObj.world.camera.is_centered:
            self.posX = self.org_pos[0] + self.camera_pos[0] - self.camera_pos_reseter[0]
            self.posY = self.org_pos[1] + self.camera_pos[1] - self.camera_pos_reseter[1]

        if gameObj.world.camera.is_centered and self.isNotMoveble == False:
            self.posX -= gameObj.world.camera.offset.x / 8
            self.posY -= gameObj.world.camera.offset.y / 8
            self.org_pos = (self.posX, self.posY)
            self.camera_pos_reseter = (self.camera_pos[0], self.camera_pos[1])


        if self.posX < -self.size[0] or self.posX > gameObj.window.window_size[0] or self.posY < -self.size[0] or self.posY > gameObj.window.window_size[1]:
            self.state = False
        elif self.type != "window":
            self.state = True


        self.rect.topleft = (self.posX, self.posY)
        self.size = self.get_sprite_size()

        if self.is_colision:
            if self.show_col == False:
                self.colision_box.fill(self.empty_col_box)
            else:
                if self.colision_box_size < self.size and (self.colision_box_pos[0] > 0 and self.colision_box_pos[1] > 0 or self.colision_box_pos[0] >= 0 and self.colision_box_pos[1] > 0 or self.colision_box_pos[0] > 0 and self.colision_box_pos[1] >= 0):

                    self.img.blit(self.colision_box, self.colision_box.get_rect())
                    pg.draw.rect(self.img, (255, 0, 0), pg.Rect(self.colision_box_pos[0], self.colision_box_pos[1], self.colision_box_size[0], self.colision_box_size[1]), 1)

                elif self.colision_box_size > self.size and (self.colision_box_pos[0] > 0 and self.colision_box_pos[1] > 0 or self.colision_box_pos[0] >= 0 and self.colision_box_pos[1] > 0 or self.colision_box_pos[0] > 0 and self.colision_box_pos[1] >= 0):
                    self.new_img.blit(self.img, (0, 0))
                    pg.draw.rect(self.new_img, (255, 0, 0), pg.Rect(self.colision_box_pos[0], self.colision_box_pos[1], self.colision_box_size[0], self.colision_box_size[1]), 1)
                    self.new_img.convert_alpha()
                    self.img = self.new_img

                if self.colision_box_pos == (0, 0):
                    self.img.blit(self.colision_box, self.colision_box.get_rect())
                    pg.draw.rect(self.colision_box, (255, 0, 0), pg.Rect(self.colision_box_pos[0], self.colision_box_pos[1], self.colision_box_size[0], self.colision_box_size[1]), 1)

    def get_sprite_size(self):
        return (self.rect[2], self.rect[3])

    def import_image(self, img_path):
        return pg.image.load(img_path).convert_alpha()
