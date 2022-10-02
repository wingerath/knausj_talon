from talon import Module, Context

mod = Module()
mod.tag("gaming_trackmania", desc="game: Trackmania")
ctx = Context()
ctx.matches = "tag: user.gaming_trackmania"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_trackmania"


