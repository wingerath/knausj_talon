from talon import Module, Context

mod = Module()
mod.tag("gaming_BatmanArkhamCity", desc="game: Batman: Arkham City")
ctx = Context()
ctx.matches = "tag: user.gaming_BatmanArkhamCity"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_BatmanArkhamCity"


