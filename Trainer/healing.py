import os
import cv2
import pyautogui
import time
import settings


class Healing:
	def __init__(self, pic_path, CHAR_NAME):
		self.pic_path = pic_path
		self.char_name = CHAR_NAME

	def ring(self, RING_HOTKEY):
		'''
		Check if there's some ring equipped
		If so, equip it
			@params
			RING_HOTKEY: hotkey to equip ring

			@return
			void
		'''
		img = os.path.join(os.path.dirname(__file__), 'imgs', 'empty_ring.png')
		template = cv2.imread(img,0)
		tmp = settings.is_visible(template, self.pic_path, False)
		x = []
		for item in tmp:
			x.extend(item)
		if x == []:
			print('- DIDN\'T PULL UP RING: SLOT NOT EMPTY!')
		else:
			print('- RING NOT FOUND! TRYING TO EQUIP')
			settings.get_tibia_active(self.char_name)
			pyautogui.press(RING_HOTKEY)


	def soft_boots(self, SOFT_HOTKEY):
		'''
		Check if there's some soft boots equipped
		If so, equip it
			@params
			SOFT_HOTKEY: hotkey to equip boots

			@return
			void
		'''
		img = os.path.join(os.path.dirname(__file__), 'imgs', 'soft_boots.png')
		template = cv2.imread(img,0)
		tmp = settings.is_visible(template, self.pic_path, False)
		x = []
		for item in tmp:
			x.extend(item)
		if x == []:
			print('- DIDN\'T EQUIP BOOTS: SLOT NOT EMPTY!')
		else:
			print('- SOFT EQUIPPED')
			settings.get_tibia_active(self.char_name)
			pyautogui.press(SOFT_HOTKEY)


	def eat_food(self, FOOD_HOTKEY):
		'''
		Eat food
			@params
			FOOD_HOTKEY: food hotkey

			@return
			void
		'''
		for _ in range(5):
			time.sleep(.5)
			pyautogui.press(FOOD_HOTKEY)