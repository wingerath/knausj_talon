from talon import Module, Context

mod = Module()
mod.tag("gaming_redDeadRedemption2", desc="game: Red Dead Redemption 2")
ctx = Context()
ctx.matches = "tag: user.gaming_redDeadRedemption2"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_redDeadRedemption2"

gaming_action_mode_redDeadRedemption2 = mod.setting(
    "my_user_file_set_gaming_action_mode_redDeadRedemption2",
    type=str,
    default="onFoot",
    desc="Set the facial action mode that should be active",
)
ctx.settings["user.my_user_file_set_gaming_action_mode_redDeadRedemption2"] = "gaming_redDeadRedemption2"


