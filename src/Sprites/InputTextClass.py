import pygame as pg


class InputTextClass:

    def __init__(self, gameObj):
        pg.sprite.Sprite.__init__(self)
        self.gameObj = gameObj
        self.inputTextList = []

    def update(self, gameObj):
        self.gameObj = gameObj

    def newInputText(self, name, pos, prio, font, font_size, font_color, bd_color, max_width, state):
        self.inputTextObj = NewInputText(self.gameObj, self, name, pos, prio, font, font_size, font_color, bd_color, max_width, state)
        self.inputTextList.append(self.inputTextObj)
        return self.inputTextObj


class NewInputText:

    def __init__(self, gameObj, inputClass, name, pos, prio, font, font_size, font_color, bd_color, max_width, state):
        self.gameObj = gameObj
        self.inputClass = inputClass
        self.inputSelected = False
        self.state = state
        self.max_width = max_width
        self.bd_color = bd_color
        self.inputText = self.gameObj.world.fontClass.addText(name, "", font, font_size, font_color, pos, prio)
        self.inputText.state = False
        self.inputData = ""
        self.inputAddedtoData = []
        self.isShift = False
        self.type = "InputText"

        self.inputBtnSurface = pg.Surface((max_width, self.inputText.spriteObj.size[1] + 6))
        pg.draw.rect(self.inputBtnSurface, self.bd_color, pg.Rect(0, 0, self.max_width - 1, self.inputBtnSurface.get_height() - 1), 2)
        self.inputBtnSurface.blit(self.inputText.spriteObj.img, (3, 6))
        self.inputTextBtn = self.gameObj.world.btnClass.newBtnImg(name + "Btn", pos, self.inputBtnSurface, prio, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
        self.spriteObj = self.inputTextBtn.spriteObj


    def update(self):
        self.inputTextBtn.state = self.state

        if self.inputSelected:

            if self.inputTextBtn.events["mouse_on_btn"] == False and self.gameObj.input.mouse_left:
                self.inputSelected = False

            for input in self.gameObj.input.inputList:
                if input not in self.inputAddedtoData:

                    if input == "left shift":
                        self.isShift = True

                    if len(input) == 1:
                        if self.isShift:
                            self.inputData += input.upper()
                        else:
                            self.inputData += input

                    if input == "space":
                        self.inputData += " "
                    if input == "backspace":
                        self.inputData = self.inputData[:-1]

                    self.inputAddedtoData.append(input)

            for input in self.inputAddedtoData:
                if input not in self.gameObj.input.inputList:
                    if input == "left shift":
                        self.isShift = False
                    del self.inputAddedtoData[self.inputAddedtoData.index(input)]

            self.change_text(self.inputData)

        self.inputText.update()
        self.inputTextBtn.update()

    def event(self):
        self.inputTextBtn.event()

        if self.inputTextBtn.events["btn_pressed"] and self.inputSelected == False:
            self.inputSelected = True

            for inputs in self.inputClass.inputTextList:
                if inputs.inputSelected and inputs.spriteObj.id != self.spriteObj.id:
                    inputs.inputSelected = False

    def change_text(self, text):
        self.inputBtnSurface.fill("#00000000")
        self.lastSizeText = self.inputText.spriteObj.size
        self.inputText.change_text(text)
        self.newSizeText = self.inputText.spriteObj.size
        #print(self.lastSizeText, self.newSizeText)
        pg.draw.rect(self.inputBtnSurface, self.bd_color, pg.Rect(0, 0, self.max_width - 1, self.inputBtnSurface.get_height() - 1), 2)
        self.inputBtnSurface.blit(self.inputText.spriteObj.img, (3, 6))
        self.inputTextBtn.img = self.inputBtnSurface
