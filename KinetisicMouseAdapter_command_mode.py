from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module, cron

mod = Module()
ctx = Context()
ctx.matches = """mode: command"""


@ctx.action_class("user")
class Actions:

    def TongueOut_on():
        """reacts to the TongueOut facial action commencing"""
        if (actions.user.isFacialActionModifierActive()):
            actions.speech.set_microphone("System Default")
            actions.user.engine_mimic("snore")
#            actions.user.microphone_select(2)
#            actions.speech.disable()
#            actions.user.sound_disable()


