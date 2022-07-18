from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.gaming_DontStarveTogether
mode: command 
and code.language: gaming_DontStarveTogether
"""


directions = []
@mod.action_class
class Actions:
    def stop_moving():
        """stops moving in the current direction"""
        if directions:
            print("stopping: [" + ", ".join(str(dir) for dir in directions) + "]")
            actions.key(" ".join(str(dir + ":up") for dir in directions))

    def start_moving():
        """resumes current direction"""
        if directions:
            print("starting: [" + ", ".join(str(dir) for dir in directions) + "]")
            actions.key(" ".join(str(dir + ":up") for dir in directions))
            actions.key(" ".join(str(dir + ":down") for dir in directions))

    def move_in_direction(direction: str):
        """Aborts all ongoing actions"""
        justStop = direction in directions
        if directions:
            actions.key(" ".join(str(dir + ":up") for dir in directions))
        directions.clear()
        if justStop:
            return
        directions.append(direction)
        print("new direction: [" + ", ".join(str(dir) for dir in directions) + "]")
        actions.key(" ".join(str(dir + ":down") for dir in directions))

    def attack():
        """Aborts all ongoing actions"""
        actions.key("ctrl:up shift:up")
        actions.key("ctrl:down")