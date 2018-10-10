from datetime import time
import win32api
from glo import dm

class Mouse_click():
    def window_Mouse(DicDoxy,nSec):
        if(DicDoxy != None):
            print(DicDoxy)
            Idox = DicDoxy["result"][0]
            Idoy = DicDoxy["result"][1]
            if(Idox < 400):
                print("识别有误")
                return
            dm.MoveTo(int(Idox), int(Idoy))
            i = dm.LeftDown()
            win32api.Sleep(nSec)
            j = dm.leftUp()
            win32api.Sleep(1000)