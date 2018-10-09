import win32gui, win32ui, win32con, win32api,os,autopy


class Mouse_click():
    def window_Mouse(handle):
        pos = (1920,1080)
        client_pos = win32gui.ScreenToClient(handle,pos)
        tmp = win32api.MAKELONG(client_pos[0]-200, client_pos[1]-200)
        win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)