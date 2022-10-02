from talon import Module, Context

mod = Module()
mod.tag("gaming_AmongUs", desc="game: Among Us")
ctx = Context()
ctx.matches = "tag: user.gaming_AmongUs"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_AmongUs"


