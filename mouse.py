
import win32api


class Mouse_click():
    def window_Mouse(dm,Doxy,nSec):
        if(Doxy != None):
            print(Doxy)
            Idox = Doxy[0]
            Idoy = Doxy[1]
            if(Idox < 400 and Idoy > 600):
                print("识别有误")
                return
            dm.MoveTo(int(Idox), int(Idoy))
            i = dm.LeftDown()
            win32api.Sleep(nSec)
            j = dm.leftUp()
            win32api.Sleep(1000)