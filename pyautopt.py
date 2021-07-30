import ctypes
import ctypes.wintypes
def movermousepara(x,y):ctypes.windll.user32.SetCursorPos(x,y)
def posicao():cursor=ctypes.wintypes.POINT();ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor));return(cursor.x, cursor.y)
