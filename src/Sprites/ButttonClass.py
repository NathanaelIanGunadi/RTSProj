import pygame as pg

class ButtonClass(pg.sprite.Sprite):

    def __init__(self, gameObj):
        pg.sprite.Sprite.__init__(self)

        self.gameObj = gameObj
        self.btnList = []
        self.mouse_released = False

    def newBtnImg(self, name, pos, img, prio, events, id_img=None):
        self.btnImgObj = NewBtnImg(self.gameObj, self, name, pos, img, prio, events, id, id_img=None)
        self.btnList.append(self.btnImgObj)
        return self.btnImgObj

    def update(self, gameObj):
        self.gameObj = gameObj


class NewBtnImg:

    def __init__(self, gameObj, btnClass, name, pos, img, prio, events, id, id_img=None):

        self.name = name
        self.pos = pos
        self.prio = prio
        self.img = img
        self.type = "btn"
        self.state = True

        self.btnClass = btnClass

        self.eventList = ["btn_pressed", "mouse_on_btn", "btn_not_pressed", "not_mouse_on_btn"]

        for i in events:
            if not i in self.eventList:
                print("ERROR, this event don't exist")
                pass

        self.events = events

        self.spriteObj = gameObj.world.spriteClass.newSprite(self.name, self.img, self.pos, "button", self.prio, self.state, id)
        self.priority = self.spriteObj.priority

        self.size = self.spriteObj.get_sprite_size()

    def event(self):

        for i in self.events:
            mouse_pos = pg.mouse.get_pos()

            if i == self.eventList[0]:
                if self.spriteObj.state == True:
                    if pg.mouse.get_pressed()[0] == True and self.btnClass.mouse_released == False:
                        if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.size[0] and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.size[1]:
                            self.events[i] = True
                            self.btnClass.mouse_released = True
                    else:
                   		self.events[i] = False

            if i == self.eventList[1]:
                if self.spriteObj.state == True:
                    if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.size[0] and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.size[1]:
                        self.events[i] = True
                    else:
                   		self.events[i] = False

            if i == self.eventList[2]:
                if self.spriteObj.state == True or self.spriteObj.state == False:
                    if pg.mouse.get_pressed()[0] == False:
                        if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.size[0] and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.size[1]:
                            self.events[i] = True
                            self.btnClass.mouse_released = False
                    else:
                    	self.events[i] = False

            if i == self.eventList[3]:
                if self.spriteObj.state == True:
                    if not mouse_pos[0] > self.pos[0] and not mouse_pos[0] < self.pos[0] + self.size[0] and not mouse_pos[1] > self.pos[1] and not mouse_pos[1] < self.pos[1] + self.size[1]:
                        self.events[i] = True
                    else:
                   		self.events[i] = False

    def update(self):
        self.pos = self.spriteObj.pos
        self.spriteObj.state = self.state
        self.spriteObj.update()
