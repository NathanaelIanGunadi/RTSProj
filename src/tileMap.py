from pytmx.util_pygame import load_pygame
from xml.dom import minidom
import pygame as pg

class TileMap:

    def __init__(self, gameObj, filename, scale):
        tmx_data = load_pygame(filename)

        self.gameObj = gameObj
        self.filename = filename

        self.get_matrix()

        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                tiles_nmb = 0
                for x, y, surf in layer.tiles():
                    pos = (x*scale, y*scale)
                    self.gameObj.world.tileClass.newTile(layer.name + "_tile" + str(tiles_nmb), surf, pos, "forground", 1, True, tiles_nmb)
                    tiles_nmb += 1

        for obj in tmx_data.objects:
            pos = obj.x, obj.y

            if obj.type == "Player":
                self.gameObj.world.playerClass.newPlayer(obj.name, pos, obj.image)

    def get_matrix(self):

        file = minidom.parse(self.filename)
        models = file.getElementsByTagName("data")
        self.map_data = models[0].firstChild.data

        self.data = self.map_data.split(",")

        start = True
        self.map_matrix = []

        for data in self.data:
            if "\n" in data:
                if not start:
                    self.map_matrix.append(row)
                start = False
                row = []
                data = data.replace("\n", "")

            data = int(data)

            row.append(int(data))

        self.map_matrix[-1].extend(row)

        
