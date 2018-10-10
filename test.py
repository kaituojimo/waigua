import win32api
import win32gui

from findpic import  FindPic
import os
from glo import dm
#找图测试
# path = os.getcwd() +"\\pic\\"
# rcsurl  = path + "imgrsc.jpg"
# imgurl = path + 'annoyanceOfGoddess.jpg'
# FindPic.matchImg(rcsurl, imgurl, 0.5)

#大漠后台按键测试
hwnd = dm.GetMousePointWindow()
# //绑定你要操作的窗口
wdname1=u"《梦幻西游》手游"
w1hd=win32gui.FindWindow(0,wdname1)
# dm_ret = dm.BindWindowEx(w1hd,"dx3","windows3","windows3",0)
dm_ret = dm.BindWindow(w1hd,"dx3","windows","windows",0)
win32api.Sleep(1000)
a=dm.GetLastError()

# ///移动到所需的窗口坐标（这里指窗口客户区坐标）
i=0
while(i<10):
    dm.MoveTo(350,350)
    i = dm.LeftDown()
    win32api.Sleep(100)
    j = dm.leftUp()
    win32api.Sleep(3000)
    i+=1
