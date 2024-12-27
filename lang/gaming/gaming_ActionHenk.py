from talon import Module, Context

mod = Module()
mod.tag("gaming_ActionHenk", desc="game: Action Henk")
ctx = Context()
ctx.matches = "tag: user.gaming_ActionHenk"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_ActionHenk"


