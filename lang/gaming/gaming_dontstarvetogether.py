from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.gamingdontstarvetogether
mode: command 
and code.language: gamingdontstarvetogether
"""

@mod.action_class
class Actions:
    def abort_action():
        """Aborts all ongoing actions"""
        actions.key("f:up ctrl:up shift:up")