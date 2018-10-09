#!/usr/bin/python
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')
#current version
print(dm.Ver())

dm.MoveTo(150,150)