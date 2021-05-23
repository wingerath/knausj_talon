from talon import Context, Module, app, actions, speech_system
from playsound import playsound

mod = Module()

modes = {
    "admin": "enable extra administration commands terminal (docker, etc)",
    "debug": "a way to force debugger commands to be loaded",
    "gdb": "a way to force gdb commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
    "windbg": "a way to force windbg commands to be loaded",
}

for key, value in modes.items():
    mod.mode(key, value)


@mod.action_class
class Actions:
    def talon_mode():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()

        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            if app.platform == "mac":
                actions.user.engine_sleep()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("switch to command mode")

    def playSound(file: str):
        """plays a sound to indicate wake up"""
        try:
            playsound(file, block = False)
        except:
            playsound('user/talon_sounds/1778__junggle__ambient-buttons/29150__junggle__btn340.wav', block = False)

    def sound_enable():
        """audio signal for enabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29065__junggle__btn255.wav')

    def sound_disable():
        """audio signal for disabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29035__junggle__btn225.wav')

    def enable_withSound():
        """ensables the speech engine with a sound"""
        actions.user.sound_enable()
        actions.speech.enable()

    def disable_withSound():
        """disables the speech engine with a sound"""
        actions.user.sound_disable()
        actions.speech.disable()

    def app_color_green():
        """colors the talon icon green"""
        app.icon_color(0, 0.7, 0, 1)#green

    def app_color_red():
        """colors the talon icon red"""
        app.icon_color(1, 0, 0, 1)#red

    def app_color_gray():
        """colors the talon icon green"""
        app.icon_color(0.5, 0.5, 0.5, 0.5)#gray

    def app_color_black():
        """colors the talon icon black"""
        app.icon_color(0.5, 0.5, 0.5, 10)#black


def dragon_mode():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            if app.platform == "mac":
                actions.user.engine_wake()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("switch to command and dictation mode")
