import pygame as pg
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Map:

    def __init__(self, gameObj):
        self.gameObj = gameObj

        self.mapList = []

    def newMap(self, name):
        self.mapObj = NewMap(self.gameObj, name)
        self.mapList.append(self.mapObj)

        self.gameObj.world.spriteClass.spriteList["map"].append(self.mapObj)

        return self.mapObj

    def update(self, gameObj):
        self.gameObj = gameObj


class NewMap:

    def __init__(self, gameObj, name):
        self.gameObj = gameObj
        self.name = name
        self.pos = (0, 0, 1)
        self.org_pos = (self.pos[0], self.pos[1])
        self.render = False
        self.select_img = pg.image.load('res/tiles/selected_tile.png').convert_alpha()

        self.map_matrix = self.gameObj.world.importMap.map_matrix

        self.grid = Grid(matrix=self.map_matrix)
        self.width, self.height = (len(self.map_matrix[0]) * 32, len(self.map_matrix) * 32)
        self.surface = pg.Surface((self.width, self.height), pg.SRCALPHA) #pg.SRCALPHA
        self.surface.fill((255, 255, 255, 10))
        self.surface.convert_alpha()

        self.spriteObj = self.gameObj.world.spriteClass.newSprite(self.name, self.surface, (self.pos[0], self.pos[1]), "map", self.pos[2], True, 0)

    def get_matrix_pos(self):
        mouse_pos = pg.mouse.get_pos()
        self.rel_pos_x = mouse_pos[0] - self.spriteObj.posX
        self.rel_pos_y = mouse_pos[1] - self.spriteObj.posY

        if self.rel_pos_x <= 0:
            self.rel_pos_x = 0
        if self.rel_pos_y <= 0:
            self.rel_pos_y = 0

        if self.rel_pos_x > self.width:
            self.rel_pos_x = self.width - 1
        if self.rel_pos_y > self.height:
            self.rel_pos_y = self.height - 1

        self.col = int(self.rel_pos_x // 32)
        self.row = int(self.rel_pos_y // 32)

        if self.row <= 0:
            self.row = 0
        if self.col <= 0:
            self.col = 0

        if self.col > len(self.map_matrix[0]) - 1:
            self.col = len(self.map_matrix[0]) - 1
        if self.row > len(self.map_matrix) - 1:
            self.row = len(self.map_matrix) - 1


    def update(self, gameObj):
        self.gameObj = gameObj
        #print(self.spriteObj.posX, self.spriteObj.posY)
        self.get_matrix_pos()
        #print(self.row, self.col)
        self.selected_tile = self.map_matrix[self.row][self.col]
        self.tile_pos = (self.spriteObj.posX + self.col * 32, self.spriteObj.posY + self.row * 32)


        self.spriteObj.update(self.gameObj)
