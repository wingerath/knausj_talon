from talon import Module, Context

mod = Module()
mod.tag("gaming_ark", desc="game: Ark: Survival Evolved")
ctx = Context()
ctx.matches = "tag: user.gaming_ark"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_ark"


