import pygame as pg
import math


class PlayerClass:

    def __init__(self, gameObj):
        pg.sprite.Sprite.__init__(self)
        self.gameObj = gameObj

        self.playersList = []

    def newPlayer(self, name, pos, img):
        self.playerObj = NewPlayer(self, self.gameObj, name, pos, img)
        self.playersList.append(self.playerObj)
        return self.playerObj

    def update(self, gameObj):
        self.gameObj = gameObj


class NewPlayer:

    def __init__(self, playerClass, gameObj, name, pos, img):
        self.gameObj = gameObj
        self.name = name
        self.pos = pos
        self.img = img

        self.entityObj = self.gameObj.world.entityClass.newEntity(self.name, self.img, self.pos, "player", 2, True,
                                                                  len(playerClass.playersList), 4, 4, 50, (32, 32))
        self.spriteObj = self.entityObj.spriteObj

        self.mapObj = self.gameObj.world.mapObj

        self.path = []

        self.distance_traveled = 0

        self.counter = 0

    def distance_check(self, diff_x, diff_y):
        reached = False

        if self.distance_traveled >= 32 or self.distance_traveled <= -32:
            reached = True

        return reached

    def get_deviation(self, pos):
        deviation_x = (self.spriteObj.posX - self.mapObj.spriteObj.posX) - pos[0] * 32
        deviation_y = (self.spriteObj.posY - self.mapObj.spriteObj.posY) - pos[1] * 32


        return deviation_x, deviation_y

    def reset_pathfinding(self):
        self.counter = 0
        self.path = []
        self.distance_traveled = 0

    def update(self, gameObj):
        self.input = self.gameObj.inputs


        if self.entityObj.isSelected:

            if gameObj.inputs.mouse.buttons_released[2]:
                self.reset_pathfinding()
                self.path = self.gameObj.world.pathfinder.create_path()
                print(self.path)
                gameObj.inputs.mouse.buttons_released[2] = False

        if self.path != [] and len(self.path) != 1:

            self.current_mat_pos = self.path[self.counter]
            self.next_mat_pos = self.path[self.counter + 1]

            diff_x, diff_y = self.next_mat_pos[0] - self.current_mat_pos[0], self.next_mat_pos[1] - self.current_mat_pos[1]

            reached = self.distance_check(diff_x, diff_y)

            if reached:
                self.counter += 1
                self.distance_traveled = 0
                if self.counter == (len(self.path) - 1):
                    self.entityObj.move_entity(0, 0)
                    self.reset_pathfinding()
            else:
                if diff_y < 0:
                    self.entityObj.move_entity(0, -self.entityObj.speed)
                    self.distance_traveled += self.entityObj.speed
                elif diff_y > 0:
                    self.entityObj.move_entity(0, self.entityObj.speed)
                    self.distance_traveled += self.entityObj.speed
                elif diff_x < 0:
                    self.entityObj.move_entity(-self.entityObj.speed, 0)
                    self.distance_traveled += self.entityObj.speed
                elif diff_x > 0:
                    self.entityObj.move_entity(self.entityObj.speed, 0)
                    self.distance_traveled += self.entityObj.speed

                if not diff_x and not diff_y:
                    self.entityObj.move_entity(0, 0)
        else:
            self.reset_pathfinding()
            self.entityObj.move_entity(0, 0)

        """if self.input.player.UP:
            self.entityObj.move_entity(0, -self.entityObj.speed)

        elif self.input.player.DOWN:
            self.entityObj.move_entity(0, self.entityObj.speed)

        elif self.input.player.LEFT:
            self.entityObj.move_entity(-self.entityObj.speed, 0)

        elif self.input.player.RIGHT:
            self.entityObj.move_entity(self.entityObj.speed, 0)
        else:
            self.entityObj.move_entity(0, 0)"""
