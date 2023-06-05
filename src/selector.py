import pygame as pg

class Selector:
    def __init__(self, gameObj):
        # pg.sprite.Group.__init__(self)
        self.gameObj = gameObj
        self.inputs = self.gameObj.inputs
        self.dragging = False
        self.selected = []

    def update(self, gameObj):
        if pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed(num_buttons=3)[0]:
            self.dragging = True
            print(self.inputs.mouse_pos)
            pg.draw.rect(pg.display.get_surface(), (255, 255, 100, 150), pg.Rect(self.initalPosX,  self.initialPosY, self.inputs.mouse_pos[0] - self.initalPosX, self.inputs.mouse_pos[1] - self.initialPosY))
            pg.display.flip()
        else:
            self.initalPosX, self.initialPosY = self.inputs.mouse_pos
            print(self.initalPosX, self.initialPosY)

        self.gameObj = gameObj


