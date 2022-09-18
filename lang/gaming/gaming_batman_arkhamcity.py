from talon import Module, Context, actions, ui, imgui, clip, settings, ctrl

import re

mod = Module()
mod.tag("BatmanArkhamCity", desc="game: Batman: Arkham City")
ctx = Context()
ctx.matches = "tag: user.BatmanArkhamCity"

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
