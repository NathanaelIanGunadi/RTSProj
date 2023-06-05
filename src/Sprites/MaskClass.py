import pygame as pg

class Mask:
    def __init__(self, gameObj):
        self.gameObj = gameObj

    def fill(self):
        self.surf_w, self.surf_h = self.new_surf.get_size()
        for x in range(self.surf_w):
            for y in range(self.surf_h):
                if self.new_surf.get_at((x, y))[0] != 0:
                    self.new_surf.set_at((x, y), 'orange')

    def update(self):

        self.player = self.gameObj.world.player
        self.player_surface = self.player.spriteObj.img
        self.obj_mask = pg.mask.from_surface(self.player_surface)
        self.new_surf = self.obj_mask.to_surface()
        self.new_surf.set_colorkey((0, 0, 0))

        self.fill()

        for point in self.obj_mask.outline():
            x = point[0] + self.player.spriteObj.posX
            y = point[1] + self.player.spriteObj.posY
            pg.draw.circle(self.gameObj.window.screen,'red',(x,y),2)
