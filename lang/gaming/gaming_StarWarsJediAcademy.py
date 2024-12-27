from talon import Module, Context

mod = Module()
mod.tag("gaming_StarWarsJediAcademy", desc="game: Star Wars: Jedi Academy")
ctx = Context()
ctx.matches = "tag: user.gaming_StarWarsJediAcademy"


ctx.settings["user.my_user_file_set_face_action_mode"] = "gaming_StarWarsJediAcademy"
ctx.settings["user.my_user_file_set_eye_tracking_mode"] = "vision"


