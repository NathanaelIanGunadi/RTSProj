import pygame as pg
from pygame.locals import *

class GUI_HotBars:

    def __init__(self, gameObj):
        pg.init()

        self.gameObj = gameObj
        self.inputs = self.gameObj.inputs
        self.input_menus = ["elements","abilities","inventory"]
        self.current_input = 0
        self.elements_hotbar_length = 4
        self.abilities_hotbar_length = 9
        self.inventory_length = 5
        self.inventory_height = 5
        self.current_element = 0
        self.current_ability = 0
        self.current_inventory_slot = pg.Vector2(0,0)
        self.SLOT_SIZE_ELEMENTS = 64
        self.SLOT_SIZE_ABILITIES = 64
        self.SLOT_SIZE_INVENTORY = 64

    def get_current_menu(self):
        return self.input_menus[self.current_input]

    def update(self):
        """
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    if self.inputs.hotkeys.SHIFT:
                        if self.current_input > 0:
                            self.current_input -= 1
                    else:
                        if self.current_input < len(self.input_menus)-1:
                            self.current_input += 1
        """

        if "ESCAPE" in self.inputs.inputsKeyUp:
            if (self.inputs.hotkeys.ESCAPE == False):
                if self.current_input < len(self.input_menus)-1:
                    self.current_input += 1
                if self.current_input == len(self.input_menus)-1:
                    self.current_input = 0
                self.inputs.inputsKeyUpClear()
            else:
                if self.current_input < 0:
                    self.current_input -= 1
                if self.current_input == 0:
                    self.current_input = len(self.input_menus)-1
                self.inputs.inputsKeyUpClear()

        if (self.get_current_menu() == "elements"):
            if self.inputs.numpad.K_1:
                self.current_element = 0
            if self.inputs.numpad.K_2:
                self.current_element = 1
            if self.inputs.numpad.K_3:
                self.current_element = 2
            if self.inputs.numpad.K_4:
                self.current_element = 3

        if (self.get_current_menu() == "abilities"):
            if self.inputs.numpad.K_1:
                self.current_ability = 0
            if self.inputs.numpad.K_2:
                self.current_ability = 1
            if self.inputs.numpad.K_3:
                self.current_ability = 2
            if self.inputs.numpad.K_4:
                self.current_ability = 3
            if self.inputs.numpad.K_5:
                self.current_ability = 4
            if self.inputs.numpad.K_6:
                self.current_ability = 5
            if self.inputs.numpad.K_7:
                self.current_ability = 6
            if self.inputs.numpad.K_8:
                self.current_ability = 7
            if self.inputs.numpad.K_9:
                self.current_ability = 8

        for ix in range(self.elements_hotbar_length):
            pg.draw.rect(self.gameObj.window.screen, (50,50,50), Rect(ix*self.SLOT_SIZE_ELEMENTS,32,self.SLOT_SIZE_ELEMENTS,self.SLOT_SIZE_ELEMENTS))
            if (self.get_current_menu() == "elements"):
                pg.draw.rect(self.gameObj.window.screen, (255,0,0), Rect(ix*self.SLOT_SIZE_ELEMENTS,32,self.SLOT_SIZE_ELEMENTS,self.SLOT_SIZE_ELEMENTS), 5, 5)
            else:
                pg.draw.rect(self.gameObj.window.screen, (255,255,255), Rect(ix*self.SLOT_SIZE_ELEMENTS,32,self.SLOT_SIZE_ELEMENTS,self.SLOT_SIZE_ELEMENTS), 5, 5)

        pg.draw.rect(self.gameObj.window.screen, (255,191,0), Rect(self.current_element*self.SLOT_SIZE_ELEMENTS,32,self.SLOT_SIZE_ELEMENTS,self.SLOT_SIZE_ELEMENTS), 5, 5)


        for ix in range(self.abilities_hotbar_length):
            pg.draw.rect(self.gameObj.window.screen, (58,136,145), Rect(self.gameObj.window.window_size[0]//4+ix*self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES//2,self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES), 0, 32)
            if (self.get_current_menu() == "abilities"):
                pg.draw.rect(self.gameObj.window.screen, (255,0,0), Rect(self.gameObj.window.window_size[0]//4+ix*self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES//2,self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES), 5, 32)
            else:
                # renders in bottom center
                #pg.draw.rect(self.gameObj.window.screen, (255,255,255), Rect(self.gameObj.window.window_size[0]//4+ix*self.SLOT_SIZE_ABILITIES,self.gameObj.window.window_size[1]-self.SLOT_SIZE_ABILITIES-32,self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES), 5, 32)
                # renders in top center
                pg.draw.rect(self.gameObj.window.screen, (255,255,255), Rect(self.gameObj.window.window_size[0]//4+ix*self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES//2,self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES), 5, 32)

        pg.draw.rect(self.gameObj.window.screen, (255,191,0), Rect(self.gameObj.window.window_size[0]//4+self.current_ability*self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES//2,self.SLOT_SIZE_ABILITIES,self.SLOT_SIZE_ABILITIES), 5, 32)
