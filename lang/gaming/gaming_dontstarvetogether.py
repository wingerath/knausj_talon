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

    def BrowsUp_on(): actions.key("f:down")
    def BrowsUp_off(): actions.key("f:up")

    # WASD
    def MouthPucker_on(): actions.key("w:down")
    def MouthPucker_off(): actions.key("w:up")

    def MouthLeft_on(): actions.key("a:down")
    def MouthLeft_off(): actions.key("a:up")

    def NoseSneer_on(): actions.key("s:down")
    def NoseSneer_off(): actions.key("s:up")

    def MouthRight_on(): actions.key("d:down")
    def MouthRight_off(): actions.key("d:up")
