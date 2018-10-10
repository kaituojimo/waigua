import win32com.client,win32gui



def _init():#初始化
    global dm
    dm = win32com.client.Dispatch('dm.dmsoft')
    global wlhd
    wdname1 = u"《梦幻西游》手游"
    wlhd = win32gui.FindWindow(0, wdname1)
    dm.BindWindow(wlhd, "dx3", "windows", "windows", 0)

def get_dm():
    return dm
def get_hwnd():
    return wlhd