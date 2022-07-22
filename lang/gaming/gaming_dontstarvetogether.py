from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
mod.tag("DST", desc="game: Don't Starve Together")
ctx = Context()
ctx.matches = "tag: user.DST"

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


@ctx.action_class("user")
class Actions:

    def BrowsUp_on():
        """reacts to the given facial action commencing"""
        actions.key("ctrl:down")

    def BrowsUp_off():
        """reacts to the given facial action stopping"""
        actions.key("ctrl:up")
