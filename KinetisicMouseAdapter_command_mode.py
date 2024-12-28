from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module, cron, speech_system

mod = Module()
ctx = Context()
ctx.matches = """mode: command"""


@ctx.action_class("user")
class Actions:

    def TongueOut_on():
        """reacts to the TongueOut facial action commencing"""
        if (actions.user.isFacialActionModifierActive()):
#            actions.sound.set_microphone("System Default")
            actions.sound.set_microphone("Analogue 1 + 2 (3- Focusrite USB Audio)")
#            actions.sound.set_microphone("Analogue 1 + 2 (Focusrite Usb Audio)")
            actions.sound.set_microphone("Krisp Microphone (Krisp Microphone)")
#            actions.sound.set_microphone("VoiceMeeter Output (VB-Audio VoiceMeeter VAIO)")
            speech_system.engine_mimic("snore")
#            actions.user.microphone_select(2)
#            actions.speech.disable()
#            actions.user.sound_disable()
            actions.user.toggle_mute()


