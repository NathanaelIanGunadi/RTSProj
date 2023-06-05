from datetime import datetime, date

from src.Sprites.SpriteClass import *
from src.Sprites.EntityClass import *
from src.Sprites.TileClass import *
from src.Sprites.FontClass import *
from src.Sprites.InputTextClass import *
from src.Sprites.ButttonClass import *
from src.Sprites.PlayerClass import PlayerClass
from src.Sprites.MapClass import Map
from src.GUI.WindowGUI import WindowGUI
from src.GUI.GUIHotbars import *
from src.GUI.TalkboxGUI import TalkboxGUI

from src.tileMap import *
from src.menu import *
from src.camera import *
from src.pathfinder import *



class World:

    def __init__(self, gameObj):
        self.gameObj = gameObj

        self.spriteClass = Sprite(self.gameObj)
        self.tileClass = TileClass(self.gameObj)
        self.entityClass = EntityClass(self.gameObj)
        self.fontClass = FontClass(self.gameObj)
        self.inputTextClass = InputTextClass(self.gameObj)
        self.btnClass = ButtonClass(self.gameObj)
        self.camera = Camera(self.gameObj)
        self.playerClass = PlayerClass(self.gameObj)
        self.gui_inputs = GUI_HotBars(self.gameObj)
        self.gui_talkbox = TalkboxGUI(self.gameObj)

        self.windowGUI = WindowGUI(self.gameObj)

        self.windowGUI = WindowGUI(self.gameObj)


        self.mapObj = Map(self.gameObj)

        self.worldSprites = self.spriteClass.spriteList

        self.assets = self.gameObj.assets


    def update(self, gameObj):
        self.gameObj = gameObj

        self.spriteClass.update(gameObj)
        self.camera.update(gameObj)
        self.gui_inputs.update()
        self.player.update(gameObj)

        if self.player.entityObj.isSelected:
            self.camera.centered_on(self.player)
        else:
            self.camera.centered_off()

        self.pathfinder.update(gameObj)

        self.prio_sprites = self.spriteClass.prio_sprites
        self.update_worldList(self.spriteClass.spriteList)


    def update_worldList(self, spriteLists):
        length = len(self.worldSprites)
        if len(spriteLists) > length:
            for spriteType in spriteLists:
                added = set(spriteLists[spriteType]) - set(self.worldSprites[spriteType])
                if added:
                    self.worldSprites[spriteType].extend(list(added))

    def init_game(self):
        self.worldInit = False
        self.init_world()

    def init_world(self):

        self.importMap = TileMap(self.gameObj, self.gameObj.assets.Map().new_test_map, 16)
        self.map = self.mapObj.newMap("test")

        self.pathfinder = Pathfinder(self.gameObj)

        self.player = self.playerClass.playersList[0]

        self.window_test = self.windowGUI.newWindow("Test Window", (50, 50, 4), (350, 240), (255, 120, 255))
