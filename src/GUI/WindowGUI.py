import pygame as pg
import random

class WindowGUI:

    def __init__(self, gameObj):
        self.gameObj = gameObj

        self.windowsList = []

    def newWindow(self, name, pos, size, color, debug=False):
        self.windowObj = NewWindow(self.gameObj, name, pos, size, color, debug)
        self.windowsList.append(self.windowObj)

        self.gameObj.world.spriteClass.spriteList["window"].append(self.windowObj)

        return self.windowObj

    def update(self, gameObj):
        self.gameObj = gameObj


class NewWindow:

    def __init__(self, gameObj, name, pos, size, color, debug=False):
        self.gameObj = gameObj
        self.id = random.randint(0, 2000000)
        self.debug = debug
        self.name_title = name
        if self.debug:
            self.name = self.name_title + " - " + self.id
        else:
            self.name = self.name_title
        self.pos = list(pos)
        self.size = size


        self.titleSize = 22
        self.titlePos = (4, -2)
        self.titleFont = pg.font.Font(self.gameObj.assets.Window().font, self.titleSize)
        self.titleText = self.titleFont.render(self.name, True, (255, 255, 255))
        self.titleRect = (self.size[0] - 16, 18)

        self.offset = pg.math.Vector2()
        self.isSelected = False
        self.isDragble = False
        self.isActive = False
        self.posWhenClicked = pg.math.Vector2()

        self.windowShow = True

        if size[0] < 128 or size[1] < 64:
            print("ERROR, the window is too small")
            return False

        self.windowSurface = pg.Surface((self.size[0] - 12, self.size[1] - 12))
        self.windowRectSize = (self.size[0] - 16, self.size[1] - 16)

        # Draw the bg of the window
        pg.draw.rect(self.windowSurface, color, (2, 2, self.windowRectSize[0], self.windowRectSize[1]))

        # Draw the titleBar
        pg.draw.rect(self.windowSurface, (0, 0, 0), (2, 2, self.titleRect[0], self.titleRect[1]))

        self.cross_pos = (self.size[0] - 30, 5)
        self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().cross).convert_alpha(), self.cross_pos)

        if self.titleText.get_size()[0] > self.titleRect[0] - 12:
            print("Error, the text is too long")
        else:
            self.windowSurface.blit(self.titleText.convert_alpha(), self.titlePos)

        self.nmb_of_width, self.nmb_of_height = self.size[0] - 32, self.size[1] - 32

        self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().topleft).convert_alpha(), (-6, -6))
        self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().topright).convert_alpha(), ((self.size[0] - 16) - 6, -6))
        self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().botleft).convert_alpha(), (-6, (self.size[1] - 16) - 6))
        self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().botright).convert_alpha(), ((self.size[0] - 16) - 6, (self.size[1] - 16) - 6))

        x, y = 10, 0
        for width in range(2):
            for i in range(self.nmb_of_width):
                if width == 0:
                    self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().top).convert_alpha(), (x, y))
                else:
                    self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().bot).convert_alpha(), (x, y))
                x += 1
            x = 10
            y += self.nmb_of_height + 16

        x, y = 0, 10
        for height in range(2):
            for i in range(self.nmb_of_height):
                if height == 0:
                    self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().left).convert_alpha(), (x, y))
                else:
                    self.windowSurface.blit(pg.image.load(self.gameObj.assets.Window().right).convert_alpha(), (x, y))
                y += 1
            y = 10
            x += self.nmb_of_width + 16



        self.spriteObj = self.gameObj.world.spriteClass.newSprite(self.name, self.windowSurface, (self.pos[0], self.pos[1]), "window", self.pos[2], True, 0)
        self.spriteObj.isNotMoveble = True

    def update(self, gameObj):
        self.gameObj = gameObj

        self.name = self.name_title + " - " + str(self.id)

        self.cross_placement = (self.pos[0] + self.cross_pos[0], self.pos[1] + self.cross_pos[1])
        self.titleBar_placement = (self.pos[0] + 2, self.pos[1] + 2, self.pos[0] + self.titleRect[0], self.pos[1] + self.titleRect[1])

        if self.gameObj.inputs.mouse.LEFTBUTTON and self.spriteObj.state:

            # For select the window
            if self.gameObj.inputs.mouse_pos[0] > self.pos[0] and self.gameObj.inputs.mouse_pos[0] < self.pos[0] + self.spriteObj.size[0]:
                if self.gameObj.inputs.mouse_pos[1] > self.pos[1] and self.gameObj.inputs.mouse_pos[1] < self.pos[1] +  self.spriteObj.size[1]:
                    if self.check_other_state_window()[0] == False:
                        self.isSelected = True

            # For closing the window
            if self.gameObj.inputs.mouse_pos[0] > self.cross_placement[0] and self.gameObj.inputs.mouse_pos[0] < self.cross_placement[0] + 12:
                if self.gameObj.inputs.mouse_pos[1] > self.cross_placement[1] and self.gameObj.inputs.mouse_pos[1] < self.cross_placement[1] + 12:
                    if not self.isDragble and self.isSelected:
                        self.spriteObj.state = False

            # IF statement for drag the window
            if self.gameObj.inputs.mouse_pos[0] > self.titleBar_placement[0] and self.gameObj.inputs.mouse_pos[0] < self.titleBar_placement[2] - 12:
                if self.gameObj.inputs.mouse_pos[1] > self.titleBar_placement[1] and self.gameObj.inputs.mouse_pos[1] < self.titleBar_placement[3]:
                    if self.check_other_state_window()[1] == False and self.check_other_state_window()[0] == False:
                        if self.isDragble == False:
                            self.posWhenClicked.x = self.gameObj.inputs.mouse_pos[0]
                            self.posWhenClicked.y = self.gameObj.inputs.mouse_pos[1]

                        self.isDragble = True
                    else:
                        self.isDragble = False

        # Change the pos of the window when it's grab
        if self.isDragble:
            self.offset.x = self.spriteObj.org_pos[0] + (self.gameObj.inputs.mouse_pos[0] - self.posWhenClicked.x)
            self.offset.y = self.spriteObj.org_pos[1] + (self.gameObj.inputs.mouse_pos[1] - self.posWhenClicked.y)

            self.spriteObj.posX = self.offset.x
            self.spriteObj.posY = self.offset.y

        # Desable the grab status
        if not self.gameObj.inputs.mouse.LEFTBUTTON and self.isDragble:
            self.isDragble = False
            self.spriteObj.org_pos = (self.spriteObj.posX, self.spriteObj.posY)

        if not self.gameObj.inputs.mouse.LEFTBUTTON and self.isSelected:
            if not (self.gameObj.inputs.mouse_pos[0] > self.pos[0] and self.gameObj.inputs.mouse_pos[0] < self.pos[0] +  self.spriteObj.size[0]):
                self.isSelected = False
            if not (self.gameObj.inputs.mouse_pos[1] > self.pos[1] and self.gameObj.inputs.mouse_pos[1] < self.pos[1] + self.spriteObj.size[1]):
                self.isSelected = False

        self.spriteObj.update(self.gameObj)
        self.pos = (self.spriteObj.posX, self.spriteObj.posY, self.pos[2])

        self.pos = list(self.pos)


    def check_other_state_window(self):
        isSelected, isDragble = False, False
        for window in self.gameObj.world.windowGUI.windowsList:
            if window.isSelected and window != self:
                isSelected = True

            if window.isDragble and window != self:
                isDragble = True

        return(isSelected, isDragble)

    def check_other_prio(self):
        list_prio = []
        for window in self.gameObj.world.windowGUI.windowsList:
            if window.windowShow:
                if not window.spriteObj.priority in list_prio:
                    list_prio.append(window.spriteObj.priority)

        list_prio.sort()

        return list_prio[-1]
