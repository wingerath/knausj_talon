from talon import Module, Context

mod = Module()
mod.tag("gaming_RedFaction", desc="game: Red Faction")
ctx = Context()
ctx.matches = "tag: user.gaming_RedFaction"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_RedFaction"


