import pygame as pg
import random
import copy

class Renderer:

    def __init__(self, gameObj):
        self.gameObj = gameObj
        self.screen = self.gameObj.window.screen
        self.windows = {}
        self.windows_id = []
        self.windows_z  = []
        self.WINDOWS_MAX_Z = 40
        self.windows_isactive_log = []
        self.debug = False

        self.dt = 0

    def windowsSortZ(self, window):
        windowZ = window.pos[2]
        self.windows_z.sort()
        allZValues = copy.deepcopy(self.windows_z)
        if self.WINDOWS_MAX_Z in allZValues:
            allZValues.pop(-1)
        if len(allZValues) > 0:
            maxZ = max(allZValues)
            window.pos[2] = maxZ+1
        else:
            window.pos[2] = 1
        if window.isActive:
            window.pos[2] = self.WINDOWS_MAX_Z

    def windowsAppend(self, window):
        if window.isSelected and window.isDragble:
            window.pos[2] = self.WINDOWS_MAX_Z
            window.isActive = True
            self.windows_isactive_log.append(window.id)
            for windowID in self.windows:
                if windowID != window.id:
                    print("window id is from another object")
                    self.windows[windowID].isActive = False
                    # new z index sorting
                    self.windowsSortZ(window)
                    print("self.windows[windowID].isActive: ",self.windows[windowID].isActive)
        else:
            if not window.isActive:
                # new z index sorting
                self.windowsSortZ(window)
            if window.isActive:
                if window.id != self.windows_isactive_log[-1]:
                    self.windows_isactive_log.clear()
                    window.isActive = False

        if window.id not in self.windows_id:
            self.windows_id.append(window.id)
        else:
            if self.debug:
                print("RENDERER UPDATE: renderer.windows_id already contains window with ID, changing ID of window")
            window.id = random.randint(0, 2000000)
            self.windows_id.append(window.id)

        if window.pos[2] not in self.windows_z:
            self.windows_z.append(window.pos[2])

        self.windows[window.id] = window

    def windowsClear(self):


        self.windows.clear()
        self.windows_id.clear()
        self.windows_z.clear()


    def update(self, gameObj):
        self.gameObj = gameObj

        self.screen.fill("#00000000")

        self.windowsClear()

        for window in self.gameObj.world.spriteClass.spriteList["window"]:
            #self.windows.append(window)
            self.windowsAppend(window)
            if self.debug:
                print("window: ", window, "\nwindow id: ", window.id, "\nwindow z: ", window.pos[2])
                print("\n", "isSelected: ", window.isSelected, "\n", "isDragble: ", window.isDragble, "\n", "isActive: ", window.isActive, "\n___________________________________________")


        self.sprites = self.gameObj.world.worldSprites
        for prio in self.gameObj.world.prio_sprites:
            for spriteType in self.sprites:
                for sprite in self.sprites[spriteType]:
                    if spriteType != "window":
                        if sprite.spriteObj.state and sprite.spriteObj.priority == prio:
                            self.screen.blit(sprite.spriteObj.img, sprite.spriteObj.rect)
                            if sprite.spriteObj.type == "map" and self.gameObj.world.camera.is_centered:
                                self.gameObj.window.screen.blit(sprite.select_img, sprite.tile_pos)
                    if spriteType == "window":
                        pass
                        # if sprite.spriteObj.state and sprite.spriteObj.priority == prio:
                            # self.screen.blit(sprite.spriteObj.img, sprite.spriteObj.rect)


        if len(self.windows) > 0:
            # print("length > 0")
            self.windows_z.sort()
            for windowZ in self.windows_z:
                # print(f"windowZ: {windowZ}")
                for windowID in self.windows:
                    # print(f"windowID: {windowID}")
                    window = self.windows[windowID]
                    # print(f"window.pos[2]: {window.pos[2]}")
                    if window.pos[2] == windowZ:
                        for prio in self.gameObj.world.prio_sprites:
                            for spriteType in self.sprites:
                                for sprite in self.sprites[spriteType]:
                                    if spriteType == "window":
                                        if sprite.spriteObj.state and sprite.spriteObj.priority == prio:
                                            if sprite.id == windowID:
                                                self.screen.blit(sprite.spriteObj.img, sprite.spriteObj.rect)
        #self.windows.clear()

        self.dt = self.gameObj.window.main_clock.tick(self.gameObj.window.fps) / 1000.0
