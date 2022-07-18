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

@mod.action_class
class Actions:
    def abort_action():
        """Aborts all ongoing actions"""
        actions.key("ctrl:up shift:up")

    def pickup():
        """Aborts all ongoing actions"""
        actions.key("ctrl:up shift:up")
        actions.key("shift:down")

    def attack():
        """Aborts all ongoing actions"""
        actions.key("ctrl:up shift:up")
        actions.key("ctrl:down")

    def test_action():
        """a test action"""
        actions.key("x")