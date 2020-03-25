import os
import cv2
import pyautogui
import time
import numpy as np
import settings


class Healing:
	def __init__(self, SS_DIRPATH, SS_HOTKEY):
		self.dir_path = SS_DIRPATH
		self.htk = SS_HOTKEY

	def ring(self, RING_HOTKEY):
		'''
		Check if there's some ring equipped
		If so, equip it
			@params
			SS_DIRPATH: Tibia screenshots path folder
			SS_HOTKEY: screenshot hotkey
			RING_HOTKEY: hotkey to equip ring

			@return
			void
		'''

		img = os.path.join(os.path.dirname(__file__), 'imgs', 'empty_ring.png')
		# template = cv2.imread('D:/Documents/git/tibia-tools/imgs/empty_ring.png',0)
		template = cv2.imread(img,0)
		tmp = settings.is_visible(template, self.dir_path, self.htk, False)
		x = []
		for item in tmp:
			x.extend(item)
		if x == []:
			print('- DIDN\'T PULL UP RING: SLOT NOT EMPTY!')
		else:
			print('- RING EQUIPPED')
			pyautogui.press(RING_HOTKEY)
			# break


	def soft_boots(self, SOFT_HOTKEY):
		'''
		Check if there's some some soft boots equipped
		If so, equip it
			@params
			SS_DIRPATH: Tibia screenshots path folder
			SS_HOTKEY: screenshot hotkey
			RING_HOTKEY: hotkey to equip boots

			@return
			void
		'''

		img = os.path.join(os.path.dirname(__file__), 'imgs', 'soft_boots.png')
		# template = cv2.imread('D:/Documents/git/tibia-tools/imgs/soft_boots.png',0)
		template = cv2.imread(img,0)
		tmp = settings.is_visible(template, self.dir_path, self.htk, False)
		x = []
		for item in tmp:
			x.extend(item)
		if x == []:
			print('- DIDN\'T EQUIP BOOTS: SLOT NOT EMPTY!')
		else:
			print('- SOFT EQUIPPED')
			pyautogui.press(SOFT_HOTKEY)
			# break


	def eat_food(self, FOOD_HOTKEY):
		'''
		Check if you are hungry
		If so, eats food
			@params
			SS_DIRPATH: Tibia screenshots path folder
			SS_HOTKEY: screenshot hotkey
			RING_HOTKEY: hotkey to eat food

			@return
			void
		'''
		img = os.path.join(os.path.dirname(__file__), 'imgs', 'hungry.png')
		# template = cv2.imread('D:/Documents/git/tibia-tools/imgs/hungry.png',0)
		template = cv2.imread(img,0)
		tmp = settings.is_visible(template, self.dir_path, self.htk, False)
		x = []
		for item in tmp:
			x.extend(item)
		if x == []:
			print('- DIDN\'T EAT FOOD: NOT HUNGRY!')
		else:
			for _ in range(5):
				pyautogui.press(FOOD_HOTKEY)
				print('- FOOD EATEN')