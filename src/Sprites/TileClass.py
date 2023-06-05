import pygame as pg


class TileClass:

	def __init__(self, gameObj):
		pg.sprite.Sprite.__init__(self)
		self.gameObj = gameObj

		self.tileType = ["forground", "background", 'air']
		self.tileList = []

	def newTile(self, name, img, pos, type, prio, state, id, col_box_size=None, col_box_pos=None):

		if type == "air":
			self.tileObj = newTile(self, name, img, pos, type, prio, state, id, col_box_size, col_box_pos)
		self.tileObj = newTile(self, name, img, pos, type, prio, state, id, col_box_size, col_box_pos)
		self.tileList.append(self.tileObj)
		self.gameObj.world.spriteClass.spriteList["tile"].append(self.tileObj)
		return self.tileObj

	def update(self, gameObj):
		self.gameObj = gameObj

class newTile:

	def __init__(self, tileClass, name, img, pos, type, prio, state, id, col_box_size=None, col_box_pos=None):

		self.tileClass = tileClass
		self.gameObj = self.tileClass.gameObj
		self.spriteClass = self.gameObj.world.spriteClass
		self.tileType = self.tileClass.tileType

		self.type = type

		if type in self.tileType:
			self.spriteObj = self.spriteClass.newSprite(name, img, pos, "tile", prio, state, id, col_box_size, col_box_pos)

	def set_state_col(self, col_state, show_col=False):
		if self.spriteObj.is_colision:
			self.spriteObj.col_state = col_state

		if show_col:
			self.spriteObj.show_col = True

	def update(self, gameObj):
		self.spriteObj.update(gameObj)
