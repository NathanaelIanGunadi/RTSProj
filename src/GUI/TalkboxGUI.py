import pygame as pg

class TalkboxGUI:

    def __init__(self, gameObj):
        self.gameObj = gameObj

        self.talkboxsList = []

    def newTalkbox(self, name, pos, size, color, debug=False):
        self.talkboxObj = NewTalkbox(self.gameObj, name, pos, size, color, debug)
        self.talkboxsList.append(self.talkboxObj)

        self.gameObj.world.spriteClass.spriteList["talkbox"].append(self.talkboxObj)

        return self.talkboxObj

    def update(self, gameObj):
        self.gameObj = gameObj


class NewTalkbox:

    def __init__(self, gameObj, name, pos, size, char, text, text_speed):
        self.gameObj = gameObj
        self.name = name
        self.pos = pos
        self.size = size
        self.char_obj = char
        self.text = text
        self.text_speed = text_speed

        self.talkboxSurface = pg.Surface((self.size[0], self.size[1]))

        self.talkboxSurface.blit(pg.image.load(self.gameObj.assets.Talkbox().topleft).convert_alpha(), (-6, -6))
        self.talkboxSurface.blit(pg.image.load(self.gameObj.assets.Talkbox().topright).convert_alpha(), ((self.size[0] - 16) - 6, -6))
        self.talkboxSurface.blit(pg.image.load(self.gameObj.assets.Talkbox().botleft).convert_alpha(), (-6, (self.size[1] - 16) - 6))
        self.talkboxSurface.blit(pg.image.load(self.gameObj.assets.Talkbox().botright).convert_alpha(), ((self.size[0] - 16) - 6, (self.size[1] - 16) - 6))

        self.spriteObj = self.gameObj.world.spriteClass.newSprite(self.name, self.windowSurface, (self.pos[0], self.pos[1]), "talkbox", self.pos[2], True, 0)
        self.spriteObj.isNotMoveble = True

    def update(self, gameObj):
        self.gameObj = gameObj
