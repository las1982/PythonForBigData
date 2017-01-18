import sys
sys.path.append("C:\Python Libs")
sys.path.append("C:\Python Libs\win32\lib")
sys.path.append("C:\Python Libs\win32com")
sys.path.append("C:\Python Libs\win32")
import win32api
import time
import math

for i in range(500):
    x = int(500+math.sin(math.pi*i/100)*500)
    y = int(500+math.cos(i)*100)
    win32api.SetCursorPos((x,y))
    time.sleep(.01)

	
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(2.01)
    win32api.SetCursorPos((x+700, y+700))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
click(10,10)
