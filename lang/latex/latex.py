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
        """Aborts all ongoing actions"""
        actions.insert("\\" + cmd + "{}")
        actions.key("left")

