from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
mod.tag("gaming_snes9x", desc="game: SNES 9x")
ctx = Context()
ctx.matches = "tag: user.gaming_snes9x"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_snes9x"


@mod.action_class
class Actions:

    def test_action():
        """a test action"""
        actions.key("x")
