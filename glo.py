import win32com.client

dm = win32com.client.Dispatch('dm.dmsoft')


def _init():#初始化
    global dm
    dm = win32com.client.Dispatch('dm.dmsoft')

def get_value():
    return dm