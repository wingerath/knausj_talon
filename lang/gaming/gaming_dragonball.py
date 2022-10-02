from talon import Module, Context

mod = Module()
mod.tag("gaming_dragonball", desc="game: Dragonball Z: Kakarot")
ctx = Context()
ctx.matches = "tag: user.gaming_dragonball"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_dragonball"


