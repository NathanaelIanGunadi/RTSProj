import pygame as pg

import spritesheet
import path_util

from src.window import *
from src.renderer import *
from src.assets import *
from src.inputs import *
from src.world import *

class Game:

    def __init__(self):
        self.window = Window(self)
        self.renderer = Renderer(self)
        self.assets = Assets(self)
        self.inputs = Inputs(self, 0)
        self.directory = path_util.get_project_directory()

        self.world = World(self)
        self.world.init_game()

    def update(self):
        self.window.update(self)
        self.inputs.update()
        self.world.update(self)
        self.renderer.update(self)

    def run(self):
        while self.window.running:
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()
