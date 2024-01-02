from talon import Module, Context, actions, ui, imgui, clip, settings, ctrl, cron
import time
from typing import Dict

import re

mod = Module()
mod.tag("gaming", desc="generic gaming stuff")
ctx = Context()
ctx.matches = "tag: user.gaming"


class Button:
    def __init__(self, name: str):
        self.name = name
        self.release_timestamp = 0  # Timestamp of when the button should be released
        self.job = None

    def increase_delay(self, increment: int, add: bool):
        # Update the release timestamp by adding the increment
        if (add):
            self.release_timestamp += increment
        else:
            self.release_timestamp = int(time.time() * 1000 + increment)

    def reset_delay(self):
        self.release_timestamp = 0

    def remaining_delay(self):
        # Calculate the remaining delay based on the current time and the release timestamp
        return max(0, int(self.release_timestamp - time.time() * 1000))  # Convert time.time() to milliseconds

buttons_map = {}


class GameMode:
    def __init__(self, initial_name: str, initial_map: Dict[str, str] = None):
        # Initialize with the provided map or an empty map
        self.name: str = initial_name or "unnamed_mode"
        self.action_to_button_map: Dict[str, str] = initial_map or {}

    def update_map(self, new_map: Dict[str, str]):
        """Updates the action-to-button map with the provided new map."""
        self.action_to_button_map = new_map

    def get_button(self, action: str) -> str:
        """Returns the button associated with a given action."""
        return self.action_to_button_map.get(action, "")



# Create a default mode instance with the predefined mappings
default_mode = GameMode("default", {
    "click": "f",
    "whatever": "s",
})

on_foot_mode = GameMode("on_foot", {
    "click": "space",
    "whatever": "d",
})

# Initialize the active mode with the default mode
active_mode = default_mode


@mod.action_class
class Actions:
    # ... [your other actions]

    def button(action: str) -> str:
        """Returns the button associated with a given action."""
        actions.app.notify(f"Current Mode: {active_mode.name}")
        return active_mode.get_button(action)

    def set_mode(mode: str):
        """Returns the button associated with a given action."""
        global active_mode
        if (mode == "default"):
            active_mode = default_mode
            actions.app.notify(f"Setting Mode: {mode}")
        elif (mode == "on_foot"):
            active_mode = on_foot_mode
            actions.app.notify(f"Setting Mode: {mode}")
        else:
            actions.app.notify(f"Unknown mode: {mode}")


    def hold_button(button_name: str, delay_increment: int = 500, add: bool = False):
        """reacts to a given facial action with an optional delay increment"""
        if button_name not in buttons_map:
            buttons_map[button_name] = Button(button_name)
        button_obj = buttons_map[button_name]

        if button_obj.job is not None:
            cron.cancel(button_obj.job)

        # Increase the delay for the button by the specified increment
        current_time_ms = time.time() * 1000  # Current time in milliseconds
        if button_obj.release_timestamp < current_time_ms:
            button_obj.release_timestamp = current_time_ms
            actions.user.push_button(button_obj.name, "down")
        button_obj.increase_delay(delay_increment, add)

        # Using lambda to release the button after the delay
        button_obj.job = cron.after(f"{button_obj.remaining_delay()}ms", lambda: actions.user.push_button(button_obj.name, "up"))




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

    def push_button(button: str, upOrDown: str):
        """pushes the provided button"""
        mouse_button = -1
        if (button == "mouse_left"):
            mouse_button = 0
        elif (button == "mouse_middle"):
            mouse_button = 1
        elif (button == "mouse_right"):
            mouse_button = 2

        if (mouse_button > -1):
            if (upOrDown == "down"):
                actions.user.mouse_drag(mouse_button)
            elif (upOrDown == "up"):
                actions.user.mouse_drag_end()
        else:
            action = button + ":" + upOrDown
            actions.key(action)
            print(action)
