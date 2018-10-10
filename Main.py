
import time,win32api,os
import winsound

from printform import PrintForm
from findpic import FindPic
import glo as gl
from mouse import Mouse_click

gl._init()
dm = gl.get_dm()
hwnd = gl.get_hwnd()
end = time.time()
taskPicList = ['fulltolove.jpg','solutionqiangqin.jpg','juanlianmessage.jpg', 'Master_collect.jpg','annoyanceOfGoddess.jpg','findPigCapture.jpg']
taskmap = {'fulltolove.jpg':'已入情帐','solutionqiangqin.jpg':'抢亲任务','Master_collect.jpg':'师门任务','juanlianmessage.jpg':'卷帘的口信','annoyanceOfGoddess.jpg':'嫦娥的烦恼','findPigCapture.jpg':'寻找天蓬',}
nextpicList = ['nextclick.jpg','fighting.jpg', 'use.jpg','buy.jpg' ,'push.jpg']
nextmap = {'nextclick.jpg':'点击下一步','fighting.jpg':'加入战斗','buy.jpg':'买个东西','use.jpg':'使用个东西','push.jpg':'上交个东西'}
path = os.getcwd() +"\\pic\\"
def formprint():
    PrintForm.window_capture(hwnd , "imgrsc.jpg")
def findpic(imgurl):
    rcsurl = path + "imgrsc.jpg"
    imgurl = path + imgurl
    start = time.time()
    return FindPic.matchImg(rcsurl, imgurl, 0.8)
def debmode():
    while(1):
        formprint()
        DicDoxy = findpic('fighting4.jpg')
        if DicDoxy is not None and DicDoxy["result"][0] < 400:
            print('战斗ing...')
            win32api.Sleep(2000)
            continue
        DicDoxy = findpic('event.jpg')
        if DicDoxy is not None :
            Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
            # winsound.Beep(2000, 10000)
            # win32api.Sleep(10000)
            continue
        # DicDoxy = findpic('blue.jpg')
        # if DicDoxy is not None:
        #     DicDoxy = findpic('bag.jpg')
        #     if DicDoxy is not None:
        #         Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
        #         win32api.Sleep(1000)
        #         formprint()
        #         DicDoxy = findpic('addblue.jpg')
        #         if DicDoxy is not None:
        #             Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
        #             win32api.Sleep(1000)
        #             formprint()
        #             DicDoxy = findpic('use2.jpg')
        #             if DicDoxy is not None:
        #                 Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
        #                 win32api.Sleep(1000)
        #                 DicDoxy = findpic('event.jpg')
        #                 if DicDoxy is not None:
        #                     Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
        #
        #     continue

        DicDoxy = findpic('hardup.jpg')
        if DicDoxy is not None:
            xy = (858, 307)
        else:
            xy = (858, 207)
        Doxy = xy;
        Mouse_click.window_Mouse(dm, Doxy, 100)
        win32api.Sleep(1000)

        for nextpic in nextpicList:
            formprint()
            DicDoxy = findpic(nextpic)
            if (DicDoxy != None):
                print(nextmap[nextpic])
                if (nextpic == 'nextclick.jpg'):
                    while (DicDoxy):
                        if (DicDoxy != None):
                            formprint()
                            DicDoxy = findpic(nextpic)
                            if (DicDoxy != None):
                                Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
                                win32api.Sleep(500)
                else:
                    DicDoxy = findpic(nextpic)
                    Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
                    win32api.Sleep(1000)
                worksuccess = 1
                break
            else:
                continue
def susmode():
    while (1):
        formprint()
        worksuccess = 0
        DicDoxy = findpic('fighting4.jpg')
        if DicDoxy is not None and DicDoxy["result"][0] < 400:
            print('战斗ing...')
            win32api.Sleep(2000)
            continue

        for taskpic in taskPicList:
            DicDoxy = findpic(taskpic)
            if (DicDoxy != None):
                print(taskmap[taskpic])
                Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
                win32api.Sleep(10000)
                formprint()
                for nextpic in nextpicList:
                    DicDoxy = findpic(nextpic)
                    if (DicDoxy != None):
                        print(nextmap[nextpic])
                        if (nextpic == 'nextclick.jpg'):
                            while (DicDoxy):
                                if (DicDoxy != None):
                                    formprint()
                                    DicDoxy = findpic(nextpic)
                                    Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
                                    win32api.Sleep(1000)
                        else:
                            DicDoxy = findpic(nextpic)
                            Mouse_click.window_Mouse(dm, DicDoxy["result"], 100)
                            win32api.Sleep(1000)
                        worksuccess = 1
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

def main():
    debmode()
if __name__ == '__main__':
  main()