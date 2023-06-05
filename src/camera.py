import pygame as pg

class Camera:

	def __init__(self, gameObj):
		self.gameObj = gameObj

		self.camera_pos = (0, 0)
		self.centered_obj = None
		self.is_centered = False

		self.camera_speed = 5

		self.offset = pg.math.Vector2()

	def move_camera(self, posX, posY):
		self.camera_pos = (self.camera_pos[0] + posX, self.camera_pos[1] + posY)

	def update(self, gameObj):
		self.gameObj = gameObj

		self.input = self.gameObj.inputs

		if not self.is_centered:
			if self.input.camera.UP:
				self.move_camera(0, self.camera_speed)

			if self.input.camera.DOWN:
				self.move_camera(0, -self.camera_speed)

			if self.input.camera.LEFT:
				self.move_camera(-self.camera_speed, 0)

			if self.input.camera.RIGHT:
				self.move_camera(self.camera_speed, 0)


	def centered_on(self, obj):
		self.obj = obj.entityObj.spriteObj
		self.is_centered = True
		self.centered_obj = obj

		self.offset.x = self.obj.rect.centerx - (self.gameObj.window.window_size[0] / 2)
		self.offset.y = self.obj.rect.centery - (self.gameObj.window.window_size[1] / 2)

	def centered_off(self):
		self.is_centered = False
