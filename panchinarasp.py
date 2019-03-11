import time 
import subprocess
import pygame
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init(frequency = 44100, channels = 64, buffer = 1024)
sound0 = pygame.mixer.Sound("home/pi/panchinasonora_raspi/test.ogg")
sound1 = pygame.mixer.Sound("home/pi/panchinasonora_raspi/c.ogg")
sound2 = pygame.mixer.Sound("home/pi/panchinasonora_raspi/b.ogg")
sound3 = pygame.mixer.Sound("home/pi/panchinasonora_raspi/v.ogg")
sound0.play(loops = 0)
sound1.play(loops = -1)
sound2.play(loops = -1)
sound3.play(loops = -1)

sound0.set_volume(1.0)
sound1.set_volume(0.0)
sound2.set_volume(0.0)
sound3.set_volume(0.0)

while True:
	if GPIO.input(10) == GPIO.HIGH:
		print("Suono 1 in riproduzione")
		sound1.set_volume(1.0)
	else:
		print("Suono 1 stop")
		sound1.set_volume(0.0)
	if GPIO.input(8) == GPIO.HIGH:
		print("Suono 2 in riproduzione")
		sound2.set_volume(1.0)
	else:
		print("Suono 2 stop")
		sound2.set_volume(0.0)
	if GPIO.input(11) == GPIO.HIGH:
		print("Suono 3 in riproduzione")
		sound3.set_volume(1.0)
	else:
		print("Suono 3 stop")
		sound3.set_volume(0.0)

