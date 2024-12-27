from talon import Module, Context

mod = Module()
mod.tag("gaming_Diablo2", desc="game: Diablo 2")
ctx = Context()
ctx.matches = "tag: user.gaming_Diablo2"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_Diablo2"


