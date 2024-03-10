from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = "mode: sleep"

@ctx.action_class("user")
class Actions:

    def TongueOut_on():
        """reacts to the TongueOut facial action commencing"""
        if (actions.user.isFacialActionModifierActive()):
#            actions.sound.set_microphone("System Default")
            actions.sound.set_microphone("Analogue 1 + 2 (Focusrite Usb Audio)")
#            actions.sound.set_microphone("Krisp Microphone (Krisp Audio)")
#            actions.sound.set_microphone("VoiceMeeter Output (VB-Audio VoiceMeeter VAIO)")
            actions.user.engine_mimic("chirp")
#            actions.user.microphone_select(2)
#            actions.speech.enable()
#            actions.user.sound_enable()
            actions.user.toggle_mute()
