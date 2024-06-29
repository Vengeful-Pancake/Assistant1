import pygame
from pygame.locals import *
from files.GeneralFunction.Save import SAVE,LOAD
import win32api
import win32con
import win32gui
from ctypes import windll

print("Program initiates")
pygame.init()
print("pygame initiate successfully")

pygame.font.init()
font=pygame.font.SysFont('None',42)
print("Get font successfully")

WindowInfo = pygame.display.Info()
WIDTH=WindowInfo.current_w
HEIGHT=WindowInfo.current_h
print("Display Info Retrieved")

SAVE(WIDTH,"WIDTH","config")
SAVE(HEIGHT,"HEIGHT","config")

pygame.display.set_caption("...")
scrwidth = LOAD("WIDTH","config")
scrheight = LOAD("HEIGHT","config")
# a transparant screen, layered on top
screen = pygame.display.set_mode((scrwidth,scrheight),pygame.FULLSCREEN) 

# ALWAYS ON TOP


hwnd = pygame.display.get_wm_info()["window"]
transparency = (255, 0, 128)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency), 0, win32con.LWA_COLORKEY)
SetWindowPos = windll.user32.SetWindowPos
SetWindowPos(hwnd, -2, 0, 0, 0, 0, 0x0001)

# Additional windows commands
# SWP_NOSIZE = 0x0001
# SWP_NOMOVE = 0x0002
# SWP_NOZORDER = 0x0004
# SWP_NOREDRAW = 0x0008
# SWP_NOACTIVATE = 0x0010
# SWP_FRAMECHANGED = 0x0020
# SWP_SHOWWINDOW = 0x0040
# SWP_HIDEWINDOW = 0x0080
# SWP_NOCOPYBITS = 0x0100
# SWP_NOOWNERZORDER = 0x0200
# SWP_NOSENDCHANGING = 0x0400

# set transparency color

#neccessary for transparant screen, add layer
clock = pygame.time.Clock()
print("Program initiated...")

print("Loading Sprites...")
egg1 = pygame.image.load("lesser_data\\Resources\\Sprite\\Egliette\\03.png")
egg2 = pygame.image.load("lesser_data\\Resources\\Sprite\\Egliette\\02.png")
egg3 = pygame.image.load("lesser_data\\Resources\\Sprite\\Egliette\\01.png")
egg4 = pygame.image.load("lesser_data\\Resources\\Sprite\\Egliette\\04.png")
eggsize = egg1.get_size()
fleta1 = pygame.image.load("lesser_data\\Resources\\Sprite\\Fleta\\HAPPY1.png")
fleta2 = pygame.image.load("lesser_data\\Resources\\Sprite\\Fleta\\HAPPY2.png")
fleta3 = pygame.image.load("lesser_data\\Resources\\Sprite\\Fleta\\BETTERTHANYOU.png")
fletasize = fleta1.get_size()
print("Done")