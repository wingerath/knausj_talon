from talon import Module, Context, actions, ui, imgui, clip, settings, ctrl, cron

import re

mod = Module()
mod.tag("gaming", desc="generic gaming stuff")
ctx = Context()
ctx.matches = "tag: user.gaming"





gaming_cronjobs = {
    "ctrl": None
}


@mod.action_class
class Actions:

    def test_whatever():
        """A simple test action"""
        actions.key("x")

    def toggle_mouse_button(button: int):
        """Releases any held mouse buttons"""
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if (button in buttons_held_down):
            actions.user.mouse_drag_end()
        else:
            actions.user.mouse_drag(button)

    def release_mouse_buttons():
        """Releases any held mouse buttons"""
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)

    def hold_button(button: str):
        """reacts to a given facial action"""
        job = gaming_cronjobs[button]
        if (job is not None):
            cron.cancel(job)
        gaming_cronjobs[button] = cron.after("500ms", lambda: actions.user.push_button(button, "up"))
        actions.user.push_button(button, "down")

    def push_button(button: str, upOrDown: str):
        """pushes the provided button"""
        actions.key(button + ":" + upOrDown)

    def isFacialActionModifierActive():
        """returns whether CheekPuff is among the currently active"""
        return actions.user.isFacialActionMode() or facialActionModifier in activeFacialActions
