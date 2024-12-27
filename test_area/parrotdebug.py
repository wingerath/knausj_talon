from talon import Module, app, actions

mod = Module()

@mod.action_class
class asdf:
    def parrot_dp(noise: str, power: float, freq: float):
        """output parrot noise as popup"""
        actions.user.hud_add_log("event", noise)
