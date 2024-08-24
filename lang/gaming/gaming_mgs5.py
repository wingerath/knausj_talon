from talon import Module, Context

mod = Module()
mod.tag("gaming_mgs5", desc="game: Metal Gear Solid 5")
ctx = Context()
ctx.matches = "tag: user.gaming_mgs5"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_mgs5"


