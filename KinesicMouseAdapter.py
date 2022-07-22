from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()

facialActionMapping = {
    #"BrowDownLeft": "ctrl:{upOrDown}",
    #"BrowDownRight": "ctrl:{upOrDown}",
    #"BrowInnerUp": "ctrl:{upOrDown}",
    #"BrowUpLeft": "ctrl:{upOrDown}",
    #"BrowUpRight": "ctrl:{upOrDown}",
    #"BrowsDown": "ctrl:{upOrDown}",
    "BrowsUp": "ctrl:{upOrDown}",
    #"CheekPuff": "shift:{upOrDown}",
    #"CheekSquintLeft": "ctrl:{upOrDown}",
    #"CheekSquintRight": "ctrl:{upOrDown}",
    #"EyeBlinkLeft": "ctrl:{upOrDown}",
    #"EyeBlinkRight": "ctrl:{upOrDown}",
    #"EyeSquintLeft": "ctrl:{upOrDown}",
    #"EyeSquintRight": "ctrl:{upOrDown}",
    #"EyeWideLeft": "ctrl:{upOrDown}",
    #"EyeWideRight": "ctrl:{upOrDown}",
    #"EyesBlink": "ctrl:{upOrDown}",
    #"EyesDown": "ctrl:{upOrDown}",
    #"EyesLeft": "ctrl:{upOrDown}",
    #"EyesRight": "ctrl:{upOrDown}",
    #"EyesSquint": "ctrl:{upOrDown}",
    #"EyesUp": "ctrl:{upOrDown}",
    #"EyesWide": "ctrl:{upOrDown}",
    #"JawForward": "ctrl:{upOrDown}",
    #"JawLeft": "ctrl:{upOrDown}",
    #"JawOpen": "ctrl:{upOrDown}",
    #"JawRight": "ctrl:{upOrDown}",
    #"MouthClose": "ctrl:{upOrDown}",
    #"MouthDimple": "ctrl:{upOrDown}",
    #"MouthDimpleLeft": "ctrl:{upOrDown}",
    #"MouthDimpleRight": "ctrl:{upOrDown}",
    #"MouthFrown": "ctrl:{upOrDown}",
    #"MouthFrownLeft": "ctrl:{upOrDown}",
    #"MouthFrownRight": "ctrl:{upOrDown}",
    #"MouthFunnel": "ctrl:{upOrDown}",
    #"MouthLeft": "ctrl:{upOrDown}",
    #"MouthLowerDown": "ctrl:{upOrDown}",
    #"MouthLowerDownLeft": "ctrl:{upOrDown}",
    #"MouthLowerDownRight": "ctrl:{upOrDown}",
    #"MouthPress": "ctrl:{upOrDown}",
    #"MouthPressLeft": "ctrl:{upOrDown}",
    #"MouthPressRight": "ctrl:{upOrDown}",
    #"MouthPucker": "ctrl:{upOrDown}",
    #"MouthRight": "ctrl:{upOrDown}",
    #"MouthRoll": "ctrl:{upOrDown}",
    #"MouthRollLower": "ctrl:{upOrDown}",
    #"MouthRollUpper": "ctrl:{upOrDown}",
    #"MouthShrugLower": "ctrl:{upOrDown}",
    #"MouthShrugUpper": "ctrl:{upOrDown}",
    #"MouthSmile": "ctrl:{upOrDown}",
    #"MouthSmileLeft": "ctrl:{upOrDown}",
    #"MouthSmileRight": "ctrl:{upOrDown}",
    #"MouthStretch": "ctrl:{upOrDown}",
    #"MouthStretchLeft": "ctrl:{upOrDown}",
    #"MouthStretchRight": "ctrl:{upOrDown}",
    #"MouthUpperUp": "ctrl:{upOrDown}",
    #"MouthUpperUpLeft": "ctrl:{upOrDown}",
    #"MouthUpperUpRight": "ctrl:{upOrDown}",
    #"NoseSneer": "ctrl:{upOrDown}",
    #"NoseSneerLeft": "ctrl:{upOrDown}",
    #"NoseSneerRight": "ctrl:{upOrDown}",
    #"TongueOut": "ctrl:{upOrDown}",
}


@mod.action_class
class Actions:
    def facialActionMapping():
        """reacts to a given facial action"""
        return facialActionMapping

    def genericFacialAction(facialAction: str, upOrDown: str):
        """reacts to a given facial action"""
        keyCombinationTemplate = actions.user.facialActionMapping().get(facialAction)
        if (keyCombinationTemplate is None):
            return # do nothing when there is no mapping

        keyCombination = keyCombinationTemplate.format(upOrDown = upOrDown)
        if (upOrDown == "down" or "{" in keyCombinationTemplate):
            actions.key(keyCombination)

    def BrowsUp():
        """reacts to a given facial action"""
        return actions.key(keyCombination)
