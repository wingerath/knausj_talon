from talon import Module, Context, actions

mod = Module()
mod.tag("gaming_SpeedRunners", desc="game: SpeedRunners")
ctx = Context()
ctx.matches = "tag: user.gaming_SpeedRunners"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_SpeedRunners"
ctx.settings["user.my_user_file_set_face_mode_use_modifier"] = False

#ctx.settings["user.my_user_file_set_eye_tracking_mode"] = "cursor"




@mod.action_class
class Actions:
    def MouthRight_on():
        """reacts to the MouthRight facial action commencing"""
        actions.key("left:up")
        actions.key("right:down")

    def MouthRight_off():
        """reacts to the MouthRight facial action stopping"""
