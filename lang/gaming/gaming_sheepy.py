from talon import Module, Context

mod = Module()
mod.tag("gaming_sheepy", desc="game: Sheepy: A Short Adventure")
ctx = Context()
ctx.matches = "tag: user.gaming_sheepy"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_sheepy"

