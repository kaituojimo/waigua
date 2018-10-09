import time
import win32gui, win32ui, win32con, win32api
import os


class PrintForm():
    def window_capture(hwnd,filename):
      #hwnd = 0x00091A0E # 窗口的编号，0号表示当前活跃窗口
      # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）00091A0E
      hwndDC = win32gui.GetWindowDC(hwnd)
      # 根据窗口的DC获取mfcDC
      mfcDC = win32ui.CreateDCFromHandle(hwndDC)
      # mfcDC创建可兼容的DC
      saveDC = mfcDC.CreateCompatibleDC()
      # 创建bigmap准备保存图片
      saveBitMap = win32ui.CreateBitmap()
      # 获取监控器信息
      MoniterDev = win32api.EnumDisplayMonitors(None, None)
      w = MoniterDev[0][2][2]
      h = MoniterDev[0][2][3]
      w= 1035
      h=800
      # print w,h　　　#图片大小
      # 为bitmap开辟空间
      saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
      # 高度saveDC，将截图保存到saveBitmap中
      saveDC.SelectObject(saveBitMap)
      # 截取从左上角（0，0）长宽为（w，h）的图片
      saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
      filename = os.getcwd() +"//pic//"+ filename
      saveBitMap.SaveBitmapFile(saveDC, filename)
