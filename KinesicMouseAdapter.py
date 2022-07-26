from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module, cron

mod = Module()
ctx = Context()

activeFacialActions = set()

facialActionMapping = {
    "BrowDownLeft": { "down": actions.user.BrowDownLeft_on, "up": actions.user.BrowDownLeft_off },
    "BrowDownRight": { "down": actions.user.BrowDownRight_on, "up": actions.user.BrowDownRight_off },
    "BrowInnerUp": { "down": actions.user.BrowInnerUp_on, "up": actions.user.BrowInnerUp_off },
    "BrowUpLeft": { "down": actions.user.BrowUpLeft_on, "up": actions.user.BrowUpLeft_off },
    "BrowUpRight": { "down": actions.user.BrowUpRight_on, "up": actions.user.BrowUpRight_off },
    "BrowsDown": { "down": actions.user.BrowsDown_on, "up": actions.user.BrowsDown_off },
    "BrowsUp": { "down": actions.user.BrowsUp_on, "up": actions.user.BrowsUp_off },
    "CheekPuff": { "down": actions.user.CheekPuff_on, "up": actions.user.CheekPuff_off },
    "CheekSquintLeft": { "down": actions.user.CheekSquintLeft_on, "up": actions.user.CheekSquintLeft_off },
    "CheekSquintRight": { "down": actions.user.CheekSquintRight_on, "up": actions.user.CheekSquintRight_off },
    "EyeBlinkLeft": { "down": actions.user.EyeBlinkLeft_on, "up": actions.user.EyeBlinkLeft_off },
    "EyeBlinkRight": { "down": actions.user.EyeBlinkRight_on, "up": actions.user.EyeBlinkRight_off },
    "EyeSquintLeft": { "down": actions.user.EyeSquintLeft_on, "up": actions.user.EyeSquintLeft_off },
    "EyeSquintRight": { "down": actions.user.EyeSquintRight_on, "up": actions.user.EyeSquintRight_off },
    "EyeWideLeft": { "down": actions.user.EyeWideLeft_on, "up": actions.user.EyeWideLeft_off },
    "EyeWideRight": { "down": actions.user.EyeWideRight_on, "up": actions.user.EyeWideRight_off },
    "EyesBlink": { "down": actions.user.EyesBlink_on, "up": actions.user.EyesBlink_off },
    "EyesDown": { "down": actions.user.EyesDown_on, "up": actions.user.EyesDown_off },
    "EyesLeft": { "down": actions.user.EyesLeft_on, "up": actions.user.EyesLeft_off },
    "EyesRight": { "down": actions.user.EyesRight_on, "up": actions.user.EyesRight_off },
    "EyesSquint": { "down": actions.user.EyesSquint_on, "up": actions.user.EyesSquint_off },
    "EyesUp": { "down": actions.user.EyesUp_on, "up": actions.user.EyesUp_off },
    "EyesWide": { "down": actions.user.EyesWide_on, "up": actions.user.EyesWide_off },
    "JawForward": { "down": actions.user.JawForward_on, "up": actions.user.JawForward_off },
    "JawLeft": { "down": actions.user.JawLeft_on, "up": actions.user.JawLeft_off },
    "JawOpen": { "down": actions.user.JawOpen_on, "up": actions.user.JawOpen_off },
    "JawRight": { "down": actions.user.JawRight_on, "up": actions.user.JawRight_off },
    "MouthClose": { "down": actions.user.MouthClose_on, "up": actions.user.MouthClose_off },
    "MouthDimple": { "down": actions.user.MouthDimple_on, "up": actions.user.MouthDimple_off },
    "MouthDimpleLeft": { "down": actions.user.MouthDimpleLeft_on, "up": actions.user.MouthDimpleLeft_off },
    "MouthDimpleRight": { "down": actions.user.MouthDimpleRight_on, "up": actions.user.MouthDimpleRight_off },
    "MouthFrown": { "down": actions.user.MouthFrown_on, "up": actions.user.MouthFrown_off },
    "MouthFrownLeft": { "down": actions.user.MouthFrownLeft_on, "up": actions.user.MouthFrownLeft_off },
    "MouthFrownRight": { "down": actions.user.MouthFrownRight_on, "up": actions.user.MouthFrownRight_off },
    "MouthFunnel": { "down": actions.user.MouthFunnel_on, "up": actions.user.MouthFunnel_off },
    "MouthLeft": { "down": actions.user.MouthLeft_on, "up": actions.user.MouthLeft_off },
    "MouthLowerDown": { "down": actions.user.MouthLowerDown_on, "up": actions.user.MouthLowerDown_off },
    "MouthLowerDownLeft": { "down": actions.user.MouthLowerDownLeft_on, "up": actions.user.MouthLowerDownLeft_off },
    "MouthLowerDownRight": { "down": actions.user.MouthLowerDownRight_on, "up": actions.user.MouthLowerDownRight_off },
    "MouthPress": { "down": actions.user.MouthPress_on, "up": actions.user.MouthPress_off },
    "MouthPressLeft": { "down": actions.user.MouthPressLeft_on, "up": actions.user.MouthPressLeft_off },
    "MouthPressRight": { "down": actions.user.MouthPressRight_on, "up": actions.user.MouthPressRight_off },
    "MouthPucker": { "down": actions.user.MouthPucker_on, "up": actions.user.MouthPucker_off },
    "MouthRight": { "down": actions.user.MouthRight_on, "up": actions.user.MouthRight_off },
    "MouthRoll": { "down": actions.user.MouthRoll_on, "up": actions.user.MouthRoll_off },
    "MouthRollLower": { "down": actions.user.MouthRollLower_on, "up": actions.user.MouthRollLower_off },
    "MouthRollUpper": { "down": actions.user.MouthRollUpper_on, "up": actions.user.MouthRollUpper_off },
    "MouthShrugLower": { "down": actions.user.MouthShrugLower_on, "up": actions.user.MouthShrugLower_off },
    "MouthShrugUpper": { "down": actions.user.MouthShrugUpper_on, "up": actions.user.MouthShrugUpper_off },
    "MouthSmile": { "down": actions.user.MouthSmile_on, "up": actions.user.MouthSmile_off },
    "MouthSmileLeft": { "down": actions.user.MouthSmileLeft_on, "up": actions.user.MouthSmileLeft_off },
    "MouthSmileRight": { "down": actions.user.MouthSmileRight_on, "up": actions.user.MouthSmileRight_off },
    "MouthStretch": { "down": actions.user.MouthStretch_on, "up": actions.user.MouthStretch_off },
    "MouthStretchLeft": { "down": actions.user.MouthStretchLeft_on, "up": actions.user.MouthStretchLeft_off },
    "MouthStretchRight": { "down": actions.user.MouthStretchRight_on, "up": actions.user.MouthStretchRight_off },
    "MouthUpperUp": { "down": actions.user.MouthUpperUp_on, "up": actions.user.MouthUpperUp_off },
    "MouthUpperUpLeft": { "down": actions.user.MouthUpperUpLeft_on, "up": actions.user.MouthUpperUpLeft_off },
    "MouthUpperUpRight": { "down": actions.user.MouthUpperUpRight_on, "up": actions.user.MouthUpperUpRight_off },
    "NoseSneer": { "down": actions.user.NoseSneer_on, "up": actions.user.NoseSneer_off },
    "NoseSneerLeft": { "down": actions.user.NoseSneerLeft_on, "up": actions.user.NoseSneerLeft_off },
    "NoseSneerRight": { "down": actions.user.NoseSneerRight_on, "up": actions.user.NoseSneerRight_off },
    "TongueOut": { "down": actions.user.TongueOut_on, "up": actions.user.TongueOut_off },
}

cronjobs = {
    "modifier_disable": None,
    "mouse_scroll": None
}
facialActionModifier = "CheekPuff"

@mod.action_class
class Actions:

    def genericFacialAction(facialAction: str, upOrDown: str):
        """reacts to a given facial action"""
        if (upOrDown == "down"):
            activeFacialActions.add(facialAction)
            if (facialAction == facialActionModifier):
                cron.cancel(cronjobs["modifier_disable"])
                cronjobs["modifier_disable"] = cron.after("1000ms", lambda: activeFacialActions.discard(facialAction))
                #elif (upOrDown == "up"): activeFacialActions.discard(facialAction)
        actionPair = facialActionMapping.get(facialAction)
        if (actionPair is None):
            return # do nothing when there is no mapping

        actionToExecute = actionPair[upOrDown]
        if (actionToExecute is None):
            return # do nothing when there is no mapping
        actionToExecute()

    def isFacialActionModifierActive():
        """returns whether CheekPuff is among the currently active i#"""
        return facialActionModifier in activeFacialActions

    def CheekPuff_on(): """reacts to the CheekPuff facial action commencing"""
    def CheekPuff_off():  """reacts to the CheekPuff facial action stopping"""

    def TongueOut_on():  """reacts to the TongueOut facial action commencing"""
    def TongueOut_off():  """reacts to the TongueOut facial action stopping"""

    def MouthPress_on():  """reacts to the MouthPress facial action commencing"""
    def MouthPress_off():  """reacts to the MouthPress facial action stopping"""

    def BrowsUp_on():  """reacts to the BrowsUp facial action commencing"""
    def BrowsUp_off():  """reacts to the BrowsUp facial action stopping"""

    def BrowsDown_on():  """reacts to the BrowsDown facial action commencing"""
    def BrowsDown_off():  """reacts to the BrowsDown facial action stopping"""


    # WASD
    def MouthPucker_on():  """reacts to the MouthPucker facial action commencing"""
    def MouthPucker_off():  """reacts to the MouthPucker facial action stopping"""

    def MouthLeft_on():  """reacts to the MouthLeft facial action commencing"""
    def MouthLeft_off():  """reacts to the MouthLeft facial action stopping"""

    def NoseSneer_on():  """reacts to the NoseSneer facial action commencing"""
    def NoseSneer_off():  """reacts to the NoseSneer facial action stopping"""

    def MouthRight_on():  """reacts to the MouthRight facial action commencing"""
    def MouthRight_off():  """reacts to the MouthRight facial action stopping"""

    def JawOpen_on():  """reacts to the JawOpen facial action commencing"""
    def JawOpen_off():  """reacts to the JawOpen facial action stopping"""


    # WASD
    def EyesUp_on():  """reacts to the EyesUp facial action commencing"""
    def EyesUp_off():  """reacts to the EyesUp facial action stopping"""

    def EyesLeft_on():  """reacts to the EyesLeft facial action commencing"""
    def EyesLeft_off():  """reacts to the EyesLeft facial action stopping"""

    def EyesDown_on():  """reacts to the EyesDown facial action commencing"""
    def EyesDown_off():  """reacts to the EyesDown facial action stopping"""

    def EyesRight_on():  """reacts to the EyesRight facial action commencing"""
    def EyesRight_off():  """reacts to the EyesRight facial action stopping"""






    def EyesWide_on():  """reacts to the EyesWide facial action commencing"""
    def EyesWide_off():  """reacts to the EyesWide facial action stopping"""

    def EyesBlink_on():  """reacts to the EyesBlink facial action commencing"""
    def EyesBlink_off():  """reacts to the EyesBlink facial action stopping"""

    def MouthStretch_on():  """reacts to the MouthStretch facial action commencing"""
    def MouthStretch_off():  """reacts to the MouthStretch facial action stopping"""

    def MouthClose_on():  """reacts to the MouthClose facial action commencing"""
    def MouthClose_off():  """reacts to the MouthClose facial action stopping"""

    def MouthDimple_on():  """reacts to the MouthDimple facial action commencing"""
    def MouthDimple_off():  """reacts to the MouthDimple facial action stopping"""

    def MouthFrown_on():  """reacts to the MouthFrown facial action commencing"""
    def MouthFrown_off():  """reacts to the MouthFrown facial action stopping"""

    def MouthFunnel_on():  """reacts to the MouthFunnel facial action commencing"""
    def MouthFunnel_off():  """reacts to the MouthFunnel facial action stopping"""

    def MouthRoll_on():  """reacts to the MouthRoll facial action commencing"""
    def MouthRoll_off():  """reacts to the MouthRoll facial action stopping"""

    def MouthSmile_on():  """reacts to the MouthSmile facial action commencing"""
    def MouthSmile_off():  """reacts to the MouthSmile facial action stopping"""






    def BrowDownLeft_on(): """reacts to the BrowDownLeft facial action commencing"""
    def BrowDownLeft_off(): """reacts to the BrowDownLeft facial action stopping"""

    def BrowDownRight_on(): """reacts to the BrowDownRight facial action commencing"""
    def BrowDownRight_off():  """reacts to the BrowDownRight facial action stopping"""

    def BrowInnerUp_on():  """reacts to the BrowInnerUp facial action commencing"""
    def BrowInnerUp_off():  """reacts to the BrowInnerUp facial action stopping"""

    def BrowUpLeft_on():  """reacts to the BrowUpLeft facial action commencing"""
    def BrowUpLeft_off():  """reacts to the BrowUpLeft facial action stopping"""

    def BrowUpRight_on():  """reacts to the BrowUpRight facial action commencing"""
    def BrowUpRight_off():  """reacts to the BrowUpRight facial action stopping"""

    def CheekSquintLeft_on():  """reacts to the CheekSquintLeft facial action commencing"""
    def CheekSquintLeft_off():  """reacts to the CheekSquintLeft facial action stopping"""

    def CheekSquintRight_on():  """reacts to the CheekSquintRight facial action commencing"""
    def CheekSquintRight_off():  """reacts to the CheekSquintRight facial action stopping"""

    def EyeBlinkLeft_on():  """reacts to the EyeBlinkLeft facial action commencing"""
    def EyeBlinkLeft_off():  """reacts to the EyeBlinkLeft facial action stopping"""

    def EyeBlinkRight_on():  """reacts to the EyeBlinkRight facial action commencing"""
    def EyeBlinkRight_off():  """reacts to the EyeBlinkRight facial action stopping"""

    def EyeSquintLeft_on():  """reacts to the EyeSquintLeft facial action commencing"""
    def EyeSquintLeft_off():  """reacts to the EyeSquintLeft facial action stopping"""

    def EyeSquintRight_on():  """reacts to the EyeSquintRight facial action commencing"""
    def EyeSquintRight_off():  """reacts to the EyeSquintRight facial action stopping"""

    def EyeWideLeft_on():  """reacts to the EyeWideLeft facial action commencing"""
    def EyeWideLeft_off():  """reacts to the EyeWideLeft facial action stopping"""

    def EyeWideRight_on():  """reacts to the EyeWideRight facial action commencing"""
    def EyeWideRight_off():  """reacts to the EyeWideRight facial action stopping"""

    def EyesSquint_on():  """reacts to the EyesSquint facial action commencing"""
    def EyesSquint_off():  """reacts to the EyesSquint facial action stopping"""

    def JawForward_on():  """reacts to the JawForward facial action commencing"""
    def JawForward_off():  """reacts to the JawForward facial action stopping"""

    def JawLeft_on():  """reacts to the JawLeft facial action commencing"""
    def JawLeft_off():  """reacts to the JawLeft facial action stopping"""

    def JawRight_on():  """reacts to the JawRight facial action commencing"""
    def JawRight_off():  """reacts to the JawRight facial action stopping"""

    def MouthDimpleLeft_on():  """reacts to the MouthDimpleLeft facial action commencing"""
    def MouthDimpleLeft_off():  """reacts to the MouthDimpleLeft facial action stopping"""

    def MouthDimpleRight_on():  """reacts to the MouthDimpleRight facial action commencing"""
    def MouthDimpleRight_off():  """reacts to the MouthDimpleRight facial action stopping"""

    def MouthFrownLeft_on():  """reacts to the MouthFrownLeft facial action commencing"""
    def MouthFrownLeft_off():  """reacts to the MouthFrownLeft facial action stopping"""

    def MouthFrownRight_on():  """reacts to the MouthFrownRight facial action commencing"""
    def MouthFrownRight_off():  """reacts to the MouthFrownRight facial action stopping"""

    def MouthLowerDown_on():  """reacts to the MouthLowerDown facial action commencing"""
    def MouthLowerDown_off():  """reacts to the MouthLowerDown facial action stopping"""

    def MouthLowerDownLeft_on():  """reacts to the MouthLowerDownLeft facial action commencing"""
    def MouthLowerDownLeft_off():  """reacts to the MouthLowerDownLeft facial action stopping"""

    def MouthLowerDownRight_on():  """reacts to the MouthLowerDownRight facial action commencing"""
    def MouthLowerDownRight_off():  """reacts to the MouthLowerDownRight facial action stopping"""

    def MouthPressLeft_on():  """reacts to the MouthPressLeft facial action commencing"""
    def MouthPressLeft_off():  """reacts to the MouthPressLeft facial action stopping"""

    def MouthPressRight_on():  """reacts to the MouthPressRight facial action commencing"""
    def MouthPressRight_off():  """reacts to the MouthPressRight facial action stopping"""

    def MouthRollLower_on():  """reacts to the MouthRollLower facial action commencing"""
    def MouthRollLower_off():  """reacts to the MouthRollLower facial action stopping"""

    def MouthRollUpper_on():  """reacts to the MouthRollUpper facial action commencing"""
    def MouthRollUpper_off():  """reacts to the MouthRollUpper facial action stopping"""

    def MouthShrugLower_on():  """reacts to the MouthShrugLower facial action commencing"""
    def MouthShrugLower_off():  """reacts to the MouthShrugLower facial action stopping"""

    def MouthShrugUpper_on():  """reacts to the MouthShrugUpper facial action commencing"""
    def MouthShrugUpper_off():  """reacts to the MouthShrugUpper facial action stopping"""

    def MouthSmileLeft_on():  """reacts to the MouthSmileLeft facial action commencing"""
    def MouthSmileLeft_off():  """reacts to the MouthSmileLeft facial action stopping"""

    def MouthSmileRight_on():  """reacts to the MouthSmileRight facial action commencing"""
    def MouthSmileRight_off():  """reacts to the MouthSmileRight facial action stopping"""

    def MouthStretchLeft_on():  """reacts to the MouthStretchLeft facial action commencing"""
    def MouthStretchLeft_off():  """reacts to the MouthStretchLeft facial action stopping"""

    def MouthStretchRight_on():  """reacts to the MouthStretchRight facial action commencing"""
    def MouthStretchRight_off():  """reacts to the MouthStretchRight facial action stopping"""

    def MouthUpperUp_on():  """reacts to the MouthUpperUp facial action commencing"""
    def MouthUpperUp_off():  """reacts to the MouthUpperUp facial action stopping"""

    def MouthUpperUpLeft_on():  """reacts to the MouthUpperUpLeft facial action commencing"""
    def MouthUpperUpLeft_off():  """reacts to the MouthUpperUpLeft facial action stopping"""

    def MouthUpperUpRight_on():  """reacts to the MouthUpperUpRight facial action commencing"""
    def MouthUpperUpRight_off():  """reacts to the MouthUpperUpRight facial action stopping"""

    def NoseSneerLeft_on():  """reacts to the NoseSneerLeft facial action commencing"""
    def NoseSneerLeft_off():  """reacts to the NoseSneerLeft facial action stopping"""

    def NoseSneerRight_on():  """reacts to the NoseSneerRight facial action commencing"""
    def NoseSneerRight_off():  """reacts to the NoseSneerRight facial action stopping"""
