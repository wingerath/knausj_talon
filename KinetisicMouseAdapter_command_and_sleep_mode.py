from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module, cron

mod = Module()
ctx = Context()
ctx.matches = ""

cronjobs = {
    "mouse_scroll": None,
}

@ctx.action_class("user")
class Actions:

    def BrowsUp_on():
        """reacts to the given facial action commencing"""
        if (actions.user.isFacialActionModifierActive()):
            actions.user.mouse_scroll_up()
            cron.cancel(cronjobs["mouse_scroll"])
            cronjobs["mouse_scroll"] = cron.interval("80ms", lambda: actions.user.mouse_scroll_up())
    def BrowsUp_off():
        """reacts to the given facial action stopping"""
        cron.cancel(cronjobs["mouse_scroll"])

    def NoseSneer_on():
        """reacts to the NoseSneer facial action commencing"""
        if (actions.user.isFacialActionModifierActive()):
            actions.user.mouse_scroll_down()
            cron.cancel(cronjobs["mouse_scroll"])
            cronjobs["mouse_scroll"] = cron.interval("80ms", lambda: actions.user.mouse_scroll_down())
    def NoseSneer_off():
        """reacts to the NoseSneer facial action stopping"""
        cron.cancel(cronjobs["mouse_scroll"])

    def MouthPress_on():
        """reacts to the NoseSneer facial action commencing"""
        if (actions.user.isFacialActionModifierActive()):
            actions.user.mouse_drag(1)
    def MouthPress_off():
        """reacts to the NoseSneer facial action stopping"""
        actions.user.mouse_drag_end()





