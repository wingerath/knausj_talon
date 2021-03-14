from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.latex
mode: command 
and code.language: latex
"""

@mod.action_class
class Actions:
    def simple_command(cmd: str):
        """inserts action_class simple_command command like \\<cmd>{{}}"""
        actions.insert("\\" + cmd + "{}")
        actions.key("left")

    def list_environment(env: str):
        """inserts a list_environment environment"""
        actions.key("enter enter")
        actions.insert("\\begin{" + env +"}\n\\item\n\\end{" + env +"}")
        actions.key("up shift-left tab end space")
