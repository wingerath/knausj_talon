from talon import Module, Context
import win32api, win32con


mod = Module()

@mod.action_class
class Actions:
    def mouse_move(dx: int, dy: int):
        """Moves the mouse"""
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)
