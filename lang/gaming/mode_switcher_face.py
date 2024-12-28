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
    elif (newMode == "gaming_RedFaction"):
        actions.key("ctrl-alt-shift-2")
    elif (newMode == "gaming_UnrealTournament"):
        actions.key("ctrl-alt-shift-3")
    elif (newMode == "gaming_secretsOfGrindea"):
        actions.key("ctrl-alt-shift-4")
    elif (newMode == "gaming_wolfenstein"):
        actions.key("ctrl-alt-shift-5")
    elif (newMode == "gaming_minecraft"):
        actions.key("ctrl-alt-shift-6")
    elif (newMode == "gaming_Diablo2"):
        actions.key("ctrl-alt-shift-7")
    elif (newMode == "gaming_snes9x"):
        actions.key("ctrl-alt-shift-o")
    elif (newMode == "gaming_redDeadRedemption2"):
        actions.key("ctrl-alt-shift-9")
    elif (newMode == "gaming_sheepy"):
        actions.key("ctrl-alt-shift-l")
    elif (newMode == "gaming_mgs5"):
        actions.key("ctrl-alt-shift-k")
    else: # Talon
        actions.key("ctrl-alt-shift-ä")
    print("facial action mode changed to: " + newMode)

def toggle_face_mode_kinesis_mouse_live():
    """Toggle project IRIS eye tracking"""
    actions.key("alt-1")
    print("toggled face mode")

def face_action_mode_handler(*args):
    """Sets the current facial action mode to the one specified in the settings"""
    newMode = settings.get("user.my_user_file_set_face_action_mode")
    change_facial_mode_kinesis_mouse_live(newMode)

@mod.action_class
class Actions:
    def set_facial_mode(newMode: str):
        """Changes the facial action mode"""
        change_facial_mode_kinesis_mouse_live(newMode)

    def toggle_face_mode():
        """Changes the facial action mode"""
        toggle_face_mode_kinesis_mouse_live()

settings.register("user.my_user_file_set_face_action_mode", face_action_mode_handler)
