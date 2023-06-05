import pygame as pg
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from xml.dom import minidom

class Pathfinder:
    def __init__(self, gameObj):
        self.gameObj = gameObj
        self.map_matrix = self.gameObj.world.importMap.map_matrix

        self.grid = Grid(matrix=self.map_matrix)

        self.path = []

        self.mapObj = self.gameObj.world.map

    def create_path(self):
        self.playerObj = self.gameObj.world.camera.centered_obj

        # self.start
        self.start_x, self.start_y = int((self.playerObj.spriteObj.posX - self.mapObj.spriteObj.posX) // 32), int((self.playerObj.spriteObj.posY - self.mapObj.spriteObj.posY) // 32)
        self.start = self.grid.node(self.start_x, self.start_y)

        # self.end
        self.end_x, self.end_y = int((self.mapObj.rel_pos_x) // 32), int((self.mapObj.rel_pos_y) // 32)
        self.end = self.grid.node(self.end_x, self.end_y)

        # path
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        self.path, _ = finder.find_path(self.start, self.end, self.grid)
        self.grid.cleanup()

        return self.path

    def empty_path(self):
        self.path = []

    def update(self, gameObj):
        self.gameObj = gameObj


