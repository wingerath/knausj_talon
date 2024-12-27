from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module, cron

mod = Module()
ctx = Context()
ctx.matches = """
tag: browser
tag: user.pdfreader
"""

facialActionState = {
    "facialActionsOn": False
}


@ctx.action_class("user")
class Actions:

#    def isFacialActionMode():
#        return facialActionState["facialActionsOn"]


    def CheekPuff_on():
        print(facialActionState["facialActionsOn"])
        facialActionState["facialActionsOn"] = not facialActionState["facialActionsOn"]
