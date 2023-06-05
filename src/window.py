import pygame as pg

class Window:

    def __init__(self, gameObj):
        pg.init()

        self.gameObj = gameObj

        flags = pg.locals.DOUBLEBUF

        self.window_size = (1280, 720)
        self.screen_size = (pg.display.Info().current_w, pg.display.Info().current_h)
        self.screen = pg.display.set_mode(self.window_size, flags, 16)

        self.fps = 60

        self.main_clock = pg.time.Clock()

        self.game_name = "GameTest"
        self.game_version = "0.1"

        pg.display.set_caption(self.game_name + " v" + self.game_version)

        self.running = True

    def update(self, gameObj):
        self.gameObj = gameObj
        pg.display.flip()
