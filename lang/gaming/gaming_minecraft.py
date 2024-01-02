from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
mod.tag("gaming_minecraft", desc="game: Minecraft")
ctx = Context()
ctx.matches = "tag: user.gaming_minecraft"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_minecraft"


@mod.action_class
class Actions:

    def test_action():
        """a test action"""
        actions.key("x")
