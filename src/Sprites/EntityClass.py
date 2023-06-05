import pygame as pg

class EntityClass:

	def __init__(self, gameObj):
		pg.sprite.Sprite.__init__(self)
		self.gameObj = gameObj

		self.entityType = ["player", "monster", "minion", "basement"]
		self.entityList = []

	def newEntity(self, name, img, pos, type, prio, state, id, velocity, speed, health, col_box_size=None, col_box_pos=None):

		self.entityObj = Entity(self, name, img, pos, type, prio, state, id, velocity, speed, health, col_box_size, col_box_pos)
		self.entityList.append(self.entityObj)
		if self.entityObj.hpBarObj != None:
			self.entityList.append(self.entityObj.hpBarObj)

		self.gameObj.world.spriteClass.spriteList["entity"].append(self.entityObj)
		self.gameObj.world.spriteClass.spriteList["hpBar"].append(self.entityObj.hpBarObj)
		return self.entityObj

	def update(self, gameObj):
		self.gameObj = gameObj
		self.entityObj.update_entityClass(self)

class Entity:

	def __init__(self, entityClass, name, img, pos, type, prio, state, id, velocity, speed, health, col_box_size, col_box_pos):

		self.entityClass = entityClass
		self.gameObj = self.entityClass.gameObj
		self.inputs = self.gameObj.inputs
		self.spriteClass = self.gameObj.world.spriteClass
		self.entityType = self.entityClass.entityType

		self.velocity = velocity
		self.direction = (0, 0)
		self.speed = speed
		self.health = health
		self.actual_health = health
		self.isMoving = False
		self.isSelected = False

		if type in self.entityType:
			self.type = type
			self.spriteObj = self.spriteClass.newSprite(name, img, pos, "entity", prio, state, id, col_box_size=col_box_size, col_box_pos=col_box_pos)

		self.hpBarObj = HpBar(self.health, self.spriteClass, name, pos, self.spriteObj.size, 3, state, id)

	def update_entityClass(self, entityClass):
		self.entityClass = entityClass

	def update(self, gameObj):

		self.entityList = self.entityClass.entityList
		self.gameObj = gameObj

		self.isEntityMoving()

		self.spriteObj.isMoving = self.isMoving
		#print(self.spriteObj.posY, self.direction)
		if self.isMoving:
			self.spriteObj.posX += self.direction[0]
			self.spriteObj.posY += self.direction[1]

		if self.gameObj.inputs.mouse.buttons_released[0]:
			if (self.spriteObj.posX <= self.gameObj.inputs.mouse_pos[0] <= self.spriteObj.posX + self.spriteObj.size[0]) and (self.spriteObj.posY <= self.gameObj.inputs.mouse_pos[1] <= self.spriteObj.posY + self.spriteObj.size[1]):
				self.isSelected = True
				self.gameObj.inputs.mouse.buttons_released[0] = False
			else:
				self.isSelected = False
				self.gameObj.inputs.mouse.buttons_released[0] = False


		self.spriteObj.update(gameObj)
		self.hpBarObj.getSpritePos(self.spriteObj.posX, self.spriteObj.posY)


	def isEntityMoving(self):
		if self.direction != (0, 0):
			self.isMoving = True
		else:
			self.isMoving = False

	def loose_hp(self, hp, entity_target):
		entity_actual_hp = 0

		for entity in self.entityList:
			if entity.spriteObj.type != "hpBar" and entity.spriteObj.spr_id == entity_target[0].spriteObj.spr_id:
				entity.actual_health -= hp
				entity_actual_hp = entity.actual_health
			else:
				entity_target[1].changeHpBar(entity_actual_hp)

	def regen_hp(self, hp, entity_target):
		entity_actual_hp = 0
		for entity in self.entityList:
			if entity.spriteObj.type != "hpBar" and entity.spriteObj.spr_id == entity_target[0].spriteObj.spr_id:
				entity.actual_health += hp
				entity_actual_hp = entity.actual_health
			else:
				entity.changeHpBar(entity_actual_hp)

	def move_entity(self, speedX, speedY):
		self.direction = (speedX, speedY)

class HpBar:

	def __init__(self, health, spriteClass, name, pos, size, prio, state, id):

		self.hpBarMaxLen = 100

		self.health = health
		self.spriteSize = size
		self.type = "hpBar"
		self.spriteClass = spriteClass

		self.hpBarSize = (100, 9)
		self.hpBarSurface = pg.Surface(self.hpBarSize)
		self.hpBarSurface.fill((0, 255, 0))
		self.spriteObj = self.spriteClass.newSprite(name + "hpBar", self.hpBarSurface, (pos[0] - (self.hpBarSize[0] / 2) + (self.spriteSize[0] / 2), pos[1] - 20), "hpBar", prio, state, id)
		self.spriteObj.isNotMoveble = True

	def getSpritePos(self, posX, posY):
		self.spritePos = (posX, posY)

	def change_max_hp(self, new_hp):
		self.health = new_hp

	def changeHpBar(self, hp):
		self.new_hpBar_size = (hp * self.hpBarMaxLen) / self.health
		self.hpBarSurface.fill((0, 0, 0))
		self.hpRect = pg.Rect(0, 0, self.new_hpBar_size, self.hpBarSize[1])
		pg.draw.rect(self.hpBarSurface, (0, 255, 0), self.hpRect)
		self.spriteObj.img = self.hpBarSurface
		self.spriteObj.update()


	def update(self, gameObj):

		self.spriteObj.posX = self.spritePos[0] - (self.hpBarSize[0] / 2) + (self.spriteSize[0] / 2)
		self.spriteObj.posY = self.spritePos[1] - 20

		self.spriteObj.update(gameObj)
