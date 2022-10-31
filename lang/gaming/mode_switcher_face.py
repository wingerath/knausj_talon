from talon import actions, app, Module, settings

mod = Module()
face_action_mode = mod.setting(
    "my_user_file_set_face_action_mode",
    type=str,
    default="Talon",
    desc="Set the facial action mode that should be active",
)

def change_facial_mode_kinesis_mouse_live(newMode: str):
    """Changes the facial action mode"""
    if (newMode == "gaming_BatmanArkhamCity"):
        actions.key("ctrl-alt-shift-ö")
    elif (newMode == "gaming_ActionHenk"):
        actions.key("ctrl-alt-shift-ß")
    elif (newMode == "gaming_AmongUs"):
        actions.key("ctrl-alt-shift-ü")
    elif (newMode == "gaming_DontStarveTogether"):
        actions.key("ctrl-alt-shift-1")
    elif (newMode == "gaming_SpeedRunners"):
        actions.key("ctrl-alt-shift-2")
    elif (newMode == "gaming_UnrealTournament"):
        actions.key("ctrl-alt-shift-3")
    elif (newMode == "gaming_gta4"):
        actions.key("ctrl-alt-shift-4")
    elif (newMode == "gaming_wolfenstein"):
        actions.key("ctrl-alt-shift-5")
    elif (newMode == "gaming_dragonball"):
        actions.key("ctrl-alt-shift-6")
    elif (newMode == "gaming_trackmania"):
        actions.key("ctrl-alt-shift-7")
    elif (newMode == "gaming_StarWarsJediAcademy"):
        actions.key("ctrl-alt-shift-8")
    else: # Talon
        actions.key("ctrl-alt-shift-ä")
    print("facial action mode changed to: " + newMode)

def toggle_face_mode_kinesis_mouse_live():
    """Toggle project IRIS eye tracking"""
    actions.key("alt-1")
    print("toggled face mode")

def face_action_mode_handler(*args):
    """Sets the current facial action mode to the one specified in the settings"""
    change_facial_mode_kinesis_mouse_live(str(face_action_mode.get()))

@mod.action_class
class Actions:
    def set_facial_mode(newMode: str):
        """Changes the facial action mode"""
        change_facial_mode_kinesis_mouse_live(newMode)

    def toggle_face_mode():
        """Changes the facial action mode"""
        toggle_face_mode_kinesis_mouse_live()

settings.register("user.my_user_file_set_face_action_mode", face_action_mode_handler)
