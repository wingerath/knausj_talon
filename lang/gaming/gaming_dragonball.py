from talon import Module, Context

mod = Module()
mod.tag("gaming_destiny", desc="game: Dragonball Z: Kakarot")
ctx = Context()
ctx.matches = "tag: user.gaming_destiny"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_destiny"


