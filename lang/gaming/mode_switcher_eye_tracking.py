from talon import actions, app, Module, settings

mod = Module()
eye_tracking_mode = mod.setting(
    "my_user_file_set_eye_tracking_mode",
    type=str,
    default="Talon",
    desc="Set the eye tracking mode that should be active",
)

eyeTrackingState = {
    "lastMode" : "Talon"
}

def set_eye_tracking_mode_mode_iris(newMode: str):
    """Changes the eye tracking mode according to the new and the last mode"""
    print(eyeTrackingState["lastMode"] + " --> " + newMode)
    lastMode = eyeTrackingState["lastMode"]
    if (newMode == lastMode):
        return;
    elif (lastMode == "vision" or newMode == "vision"):
        actions.user.eye_tracking_vision_toggle()
    elif (lastMode == "cursor" or newMode == "cursor"):
        actions.user.toggle_eye_tracking_cursor()
    else:
        return;
    print("updating last value to: " + eyeTrackingState["lastMode"])
    eyeTrackingState["lastMode"] = eye_tracking_mode.get()

def eye_tracking_cursor_toggle_iris():
    """Toggle project IRIS eye tracking"""
    actions.key("ctrl-alt-shift-f4")
    print("toggled eye tracking cursor")

def eye_tracking_vision_toggle_iris():
    """Toggle project IRIS FPS interactor"""
    actions.key("f8")
    print("toggled eye tracking vision interactor")

def eye_tracking_mode_handler(*args):
    """Sets the current facial action mode to the one specified in the settings"""
    set_eye_tracking_mode_mode_iris(str(eye_tracking_mode.get()))

@mod.action_class
class Actions:
    def toggle_eye_tracking_cursor():
        """Changes the facial action mode"""
        eye_tracking_cursor_toggle_iris()

    def eye_tracking_vision_toggle():
        """Changes the facial action mode"""
        eye_tracking_vision_toggle_iris()

settings.register("user.my_user_file_set_eye_tracking_mode", eye_tracking_mode_handler)
