from talon import Module, Context

mod = Module()
mod.tag("gaming_mgs", desc="game: Metal Gear Solid 1")
ctx = Context()
ctx.matches = "tag: user.gaming_mgs"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_mgs"


