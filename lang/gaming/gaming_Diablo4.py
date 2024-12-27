from talon import Module, Context

mod = Module()
mod.tag("gaming_Diablo4", desc="game: Diablo 2")
ctx = Context()
ctx.matches = "tag: user.gaming_Diablo4"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_Diablo4"


