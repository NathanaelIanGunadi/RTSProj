import pygame as pg
from pygame.locals import *

class InputsCardinal:
    def __init__(self):
        self.UP    = False
        self.DOWN  = False
        self.LEFT  = False
        self.RIGHT = False

class InputsPlayer(InputsCardinal):
    def __init__(self):
        super().__init__()

class InputsCamera(InputsCardinal):
    def __init__(self):
        super().__init__()
        self.ZOOMIN  = False
        self.ZOOMOUT = False
        self.CENTERED = False

class InputsMouse():
    def __init__(self):
        self.LEFTBUTTON   = False
        self.MIDDLEBUTTON = False
        self.RIGHTBUTTON  = False
        self.mouse_released = False

class InputsNumpad():
    def __init__(self):
        self.K_0 = False
        self.K_1 = False
        self.K_2 = False
        self.K_3 = False
        self.K_4 = False
        self.K_5 = False
        self.K_6 = False
        self.K_7 = False
        self.K_8 = False
        self.K_9 = False

class InputsHotkeys():
    def __init__(self):
        self.ESCAPE = False
        self.SHIFT  = False
        self.CTRL   = False
        self.ALT    = False
        self.TAB    = False



class Inputs:

    def __init__(self, gameObj, player_id):
        self.gameObj = gameObj
        self.player_id = player_id
        self.player = InputsPlayer()
        self.camera = InputsCamera()
        self.mouse  = InputsMouse()
        self.numpad = InputsNumpad()
        self.hotkeys = InputsHotkeys()
        self.inputsKeyUp = []
        self.mouse.buttons_released = [False, False, False]

    def update(self):
        self.event()

    def event(self):

        # edited

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameObj.window.running = False

            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if (keys[K_LCTRL] or keys[K_LALT]) and (keys[K_q] or keys[K_w]):
                    self.gameObj.window.running = False

                if event.key == K_w:
                    self.player.UP    = True
                if event.key == K_a:
                    self.player.LEFT  = True
                if event.key == K_s:
                    self.player.DOWN  = True
                if event.key == K_d:
                    self.player.RIGHT = True

                if event.key == K_UP:
                    self.camera.UP      = True
                if event.key == K_LEFT:
                    self.camera.LEFT    = True
                if event.key == K_DOWN:
                    self.camera.DOWN    = True
                if event.key == K_RIGHT:
                    self.camera.RIGHT   = True
                if event.key == K_MINUS:
                    self.camera.ZOOMOUT = True
                if event.key == K_PLUS:
                    self.camera.ZOOMIN  = True
                if event.key == K_f:
                    self.camera.CENTERED = True

                if event.key == K_0:
                    self.numpad.K_0 = True
                if event.key == K_1:
                    self.numpad.K_1 = True
                if event.key == K_2:
                    self.numpad.K_2 = True
                if event.key == K_3:
                    self.numpad.K_3 = True
                if event.key == K_4:
                    self.numpad.K_4 = True
                if event.key == K_5:
                    self.numpad.K_5 = True
                if event.key == K_6:
                    self.numpad.K_6 = True
                if event.key == K_7:
                    self.numpad.K_7 = True
                if event.key == K_8:
                    self.numpad.K_8 = True
                if event.key == K_9:
                    self.numpad.K_9 = True

                if event.key == K_ESCAPE:
                    self.hotkeys.ESCPAE = True
                if event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.hotkeys.SHIFT  = True
                if event.key == K_LCTRL  or event.key == K_RCTRL:
                    self.hotkeys.CTRL   = True
                if event.key == K_LALT   or event.key == K_RALT:
                    self.hotkeys.ALT    = True
                if event.key == K_TAB:
                    self.hotkeys.TAB    = True


            if event.type == pg.KEYUP:

                if event.key == K_w:
                    self.player.UP    = False
                if event.key == K_a:
                    self.player.LEFT  = False
                if event.key == K_s:
                    self.player.DOWN  = False
                if event.key == K_d:
                    self.player.RIGHT = False

                if event.key == K_UP:
                    self.camera.UP    =   False
                if event.key == K_LEFT:
                    self.camera.LEFT  =   False
                if event.key == K_DOWN:
                    self.camera.DOWN  =   False
                if event.key == K_RIGHT:
                    self.camera.RIGHT =   False
                if event.key == K_MINUS:
                    self.camera.ZOOMOUT = False
                if event.key == K_PLUS:
                    self.camera.ZOOMIN  = False
                if event.key == K_f:
                    self.camera.CENTERED  = False

                if event.key == K_0:
                    self.numpad.K_0 = False
                if event.key == K_1:
                    self.numpad.K_1 = False
                if event.key == K_2:
                    self.numpad.K_2 = False
                if event.key == K_3:
                    self.numpad.K_3 = False
                if event.key == K_4:
                    self.numpad.K_4 = False
                if event.key == K_5:
                    self.numpad.K_5 = False
                if event.key == K_6:
                    self.numpad.K_6 = False
                if event.key == K_7:
                    self.numpad.K_7 = False
                if event.key == K_8:
                    self.numpad.K_8 = False
                if event.key == K_9:
                    self.numpad.K_9 = False


                if event.key == K_ESCAPE:
                    self.hotkeys.ESCAPE = False
                    self.inputsKeyUp.append("ESCAPE")
                if event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.hotkeys.SHIFT  = False
                    self.inputsKeyUp.append("SHIFT")
                if event.key == K_LCTRL  or event.key == K_RCTRL:
                    self.hotkeys.CTRL   = False
                    self.inputsKeyUp.append("CTRL")
                if event.key == K_LALT   or event.key == K_RALT:
                    self.hotkeys.ALT    = False
                    self.inputsKeyUp.append("ALT")
                if event.key == K_TAB:
                    self.hotkeys.TAB    = False
                    self.inputsKeyUp.append("TAB")


            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse.buttons = pg.mouse.get_pressed()
                self.mouse_pos = pg.mouse.get_pos()

                if self.mouse.buttons[0]:
                    self.mouse.LEFTBUTTON   = True
                if self.mouse.buttons[1]:
                    self.mouse.MIDDLEBUTTON = True
                if self.mouse.buttons[2]:
                    self.mouse.RIGHTBUTTON  = True


            if event.type == pg.MOUSEBUTTONUP:
                self.mouse.buttons_released = [False, False, False]
                self.mouse.buttons2 = pg.mouse.get_pressed()

                for i in range(3):
                    if self.mouse.buttons[i] != self.mouse.buttons2[i]:
                        self.mouse.buttons_released[i] = True

                print(self.mouse.buttons_released, self.mouse.buttons)

                self.mouse_pos = pg.mouse.get_pos()

                if self.mouse.buttons2[0] == False:
                    self.mouse.LEFTBUTTON   = False
                if self.mouse.buttons2[1] == False:
                    self.mouse.MIDDLEBUTTON = False
                if self.mouse.buttons2[2] == False:
                    self.mouse.RIGHTBUTTON  = False

            self.mouse_pos = pg.mouse.get_pos()

    def inputsKeyUpClear(self):
        self.inputsKeyUp.clear()
