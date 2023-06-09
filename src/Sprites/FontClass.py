import pygame as pg


class FontClass:

    def __init__(self, gameObj):
        pg.sprite.Sprite.__init__(self)
        self.gameObj = gameObj
        self.textList = []

    def addText(self, name, text, font, size, color, pos, prio):
        self.fontObj = NewFont(self.gameObj, self, name, text, font, size, color, pos, prio)
        self.textList.append(self.fontObj)
        return self.fontObj

    def update(self, gameObj):
        self.gameObj = gameObj

        for font_obj in self.textList:
            font_obj.update_textClass(self)

    def change_text(self, text_name, new_text):
        for text in self.textList:
            if text.name == text_name:
                text.change_text(new_text)


class NewFont:

    def __init__(self, gameObj, fontClass, name, text, font, size, color, pos, prio):
        self.gameObj = gameObj
        self.fontClass = fontClass

        self.name = name
        self.font = pg.font.Font(font, size)
        self.pos = pos
        self.color = color
        self.text = self.font.render(text, True, color)
        self.state = True
        self.type = "text"
        self.prio = prio

        self.spriteObj = self.gameObj.world.spriteClass.newSprite(self.name, self.text, self.pos, self.type, self.prio, self.state, "#0")
        self.spriteObj.isNotMoveble = True
        self.update()

    def update_textClass(self, textClass):
        self.fontClass = textClass

    def update(self):
        self.gameObj = self.fontClass.gameObj
        self.textList = self.fontClass.textList
        self.spriteObj.state = self.state

        self.spriteObj.update()

    def change_text(self, text):
        self.text = self.font.render(text, True, self.color)
        self.spriteObj.img = self.text
        self.spriteObj.update()
