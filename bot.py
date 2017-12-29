#! /bin/python

from threading import *
from multiprocessing import Process
import time
import os

from PIL import ImageGrab
import pyautogui

print("START BOT")


coord_out = (200,1000)
out_bg = ImageGrab.grab().getpixel(coord_out) 

#COORDENADA DE --- A
coord_a = (289,877)
a_bg = ImageGrab.grab().getpixel(coord_a) 

#COORDENADA DE --- S
coord_s = (355,887)
s_bg = ImageGrab.grab().getpixel(coord_s)

#COORDENADA DE --- J
coord_j = (421,887)
j_bg = ImageGrab.grab().getpixel(coord_j)

#COORDENADA DE --- K
coord_k = (488,887)
k_bg = ImageGrab.grab().getpixel(coord_k)

#COORDENADA DE --- L
coord_l = (555,887)
l_bg = ImageGrab.grab().getpixel(coord_l)

def detect_note(screen,coord,button_bg,button,coord_out,out_bg):
	color = screen.getpixel(coord)
	out = screen.getpixel(coord_out)
	if color != button_bg and out == out_bg:
		time.sleep(0.13)
		pyautogui.press(button)
		print("--------------------",button,"------------------- \n")


if __name__ == "__main__":
	# screen = ImageGrab.grab()
	# print(time.clock(),screen.getbbox())
	# screen.save("gflash2.jpeg",'jpeg')

	while True:		
		time.sleep(0.01)
		screen = ImageGrab.grab()

		t1 = Thread(target = detect_note,args=(screen,coord_a,a_bg,'a',coord_out,out_bg,))
		t2 = Thread(target = detect_note,args=(screen,coord_s,s_bg,'s',coord_out,out_bg,))
		t3 = Thread(target = detect_note,args=(screen,coord_j,j_bg,'j',coord_out,out_bg,))
		t4 = Thread(target = detect_note,args=(screen,coord_k,k_bg,'k',coord_out,out_bg,))
		t5 = Thread(target = detect_note,args=(screen,coord_l,l_bg,'l',coord_out,out_bg,))

		t1.setDaemon(True)
		t2.setDaemon(True)
		t3.setDaemon(True)
		t4.setDaemon(True)
		t5.setDaemon(True)

		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
