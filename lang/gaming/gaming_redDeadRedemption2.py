from talon import Module, Context

mod = Module()
mod.tag("gaming_redDeadRedemption2", desc="game: Red Dead Redemption 2")
ctx = Context()
ctx.matches = "tag: user.gaming_redDeadRedemption2"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_redDeadRedemption2"


