#import aircv as ac
import time
import win32com.client
from printform import PrintForm
from findpic import FindPic
import win32gui, win32ui, win32con, win32api,os,autopy
from mouse import Mouse_click

dm = win32com.client.Dispatch('dm.dmsoft')
end = time.time()
path = os.getcwd() +"//pic//"
wdname1=u"《梦幻西游》手游"
w1hd=win32gui.FindWindow(0,wdname1)


PrintForm.window_capture(w1hd,"imgrsc.jpg")
rcsurl = path+"imgrsc.jpg"
#imgurl = path+"Master_collect.jpg"
imgurl = path+"fighting.jpg"
start = time.time()
DicDoxy = {}

DicDoxy = FindPic.matchImg(rcsurl,imgurl,0.6)
Idox = 0
Idoy = 0
if(DicDoxy != None):
    Idox = DicDoxy["result"][0]
    Idoy = DicDoxy["result"][1]
    autopy.mouse.move(150, 150)
    #win32api.SetCursorPos((int(Idox), int(Idoy)))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(Idox), int(Idoy), 0, 0)
    autopy.mouse.smooth_move(int(Idox)+30, int(Idoy)+30)
    i = dm.LeftDown()
    win32api.Sleep(500)
    j = dm.leftUp()
    z=dm.LeftClick
    print(i,j,z)
end = time.time()
timeuse = end - start
print(timeuse)
#Mouse_click.window_Mouse(w1hd)