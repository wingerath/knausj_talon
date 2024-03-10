from talon import Module, Context, actions, ui, imgui, clip, settings, ctrl, cron
import time
from typing import Dict

import re

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def toggle_mute():
        """A simple test action"""
        actions.key("ctrl-shift-space")
