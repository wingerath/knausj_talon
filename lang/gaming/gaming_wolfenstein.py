from talon import Module, Context

mod = Module()
mod.tag("gaming_wolfenstein", desc="game: Wolfenstein")
ctx = Context()
ctx.matches = "tag: user.gaming_wolfenstein"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_wolfenstein"

ctx.settings["user.my_user_file_set_eye_tracking_mode"] = "vision"

