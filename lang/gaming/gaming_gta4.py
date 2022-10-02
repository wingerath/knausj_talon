from talon import Module, Context

mod = Module()
mod.tag("gaming_gta4", desc="game: GTA IV")
ctx = Context()
ctx.matches = "tag: user.gaming_gta4"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_gta4"


