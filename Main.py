#import aircv as ac
import time
import win32com.client
from printform import PrintForm
from findpic import FindPic
import win32gui, win32ui, win32con, win32api,os,autopy
from mouse import Mouse_click
from glo import dm
from mouse import Mouse_click
# global dm
# dm = win32com.client.Dispatch('dm.dmsoft')
end = time.time()
taskPicList = ['juanlianmessage.jpg', 'Master_collect.jpg','annoyanceOfGoddess.jpg','findPigCapture.jpg']
taskmap = {'Master_collect.jpg':'师门任务','juanlianmessage.jpg':'卷帘的口信','annoyanceOfGoddess.jpg':'嫦娥的烦恼','findPigCapture.jpg':'寻找天蓬',}
nextpicList = ['nextclick.jpg','fighting.jpg', 'use.jpg','buy.jpg' ,'push.jpg']
nextmap = {'nextclick.jpg':'点击下一步','fighting.jpg':'加入战斗','buy.jpg':'买个东西','use.jpg':'使用个东西','push.jpg':'上交个东西'}
path = os.getcwd() +"\\pic\\"
wdname1=u"《梦幻西游》手游"
w1hd=win32gui.FindWindow(0,wdname1)
def formprint():
    PrintForm.window_capture(w1hd, "imgrsc.jpg")
def findpic(imgurl):
    rcsurl = path + "imgrsc.jpg"
    imgurl = path + imgurl
    start = time.time()

    return FindPic.matchImg(rcsurl, imgurl, 0.8)
while(1):
    formprint()
    Idox = 0
    Idoy = 0
    DicDoxy = {}
    worksuccess = 0
    DicDoxy = findpic('fighting4.jpg')
    if DicDoxy is not None and DicDoxy["result"][0]<400:
        print('战斗ing...')
        win32api.Sleep(2000)
        continue


    for taskpic in taskPicList:
        DicDoxy = findpic(taskpic)
        if (DicDoxy != None):
            print(taskmap[taskpic])
            Mouse_click.window_Mouse(DicDoxy,100)
            win32api.Sleep(10000)
            formprint()
            for nextpic in nextpicList:
                DicDoxy = findpic(nextpic)
                if (DicDoxy != None):
                    print(nextmap[nextpic])
                    if(nextpic == 'nextclick.jpg'):
                        while(DicDoxy):
                            if(DicDoxy != None):
                                formprint()
                                DicDoxy = findpic(nextpic)
                                Mouse_click.window_Mouse(DicDoxy,100)
                                win32api.Sleep(1000)
                    else:
                        DicDoxy = findpic(nextpic)
                        Mouse_click.window_Mouse(DicDoxy, 100)
                        win32api.Sleep(1000)
                    worksuccess =1
                    break
                else:
                    continue
            if worksuccess == 1:
                break
        else:
            continue
    win32api.Sleep(5000)
end = time.time()
timeuse = end - start
print(timeuse)
#Mouse_click.window_Mouse(w1hd)