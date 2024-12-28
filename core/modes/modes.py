from talon import Context, Module, actions, app, speech_system, cron
import sounddevice as sd
import soundfile as sf
import threading
import queue


mod = Module()
ctx_sleep = Context()
ctx_awake = Context()

modes = {
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
}

for key, value in modes.items():
    mod.mode(key, value)

ctx_sleep.matches = r"""
mode: sleep
"""

ctx_awake.matches = r"""
not mode: sleep
"""

class SoundPlayer:
    def __init__(self):
        self.queue = queue.Queue()
        self.running = False
        self.cron_job = None

    def _play_sound_task(self):
        try:
            filename = self.queue.get_nowait()
            if filename == "exit":
                self.stop()
                return
            data, samplerate = sf.read(filename, dtype="float32")
            sd.play(data, samplerate)
            sd.wait()
        except queue.Empty:
            pass  # No sounds to play, continue polling

    def play(self, filename):
        """Add a sound file to the queue and start the cron job if not running."""
        self.queue.put(filename)
        if not self.running:
            self.running = True
            self.cron_job = cron.interval("30ms", self._play_sound_task)

    def stop(self):
        """Stop the sound player and clean up."""
        if self.running:
            self.queue.put("exit")
            self.running = False
            if self.cron_job:
                cron.cancel(self.cron_job)
                self.cron_job = None


# Example usage
player = SoundPlayer()
app.register("ready", lambda: player.stop())  # Ensure player stops when Talon reloads


@ctx_sleep.action_class("speech")
class ActionsSleepMode:
    def disable():
        actions.app.notify("Talon is already asleep")


@ctx_awake.action_class("speech")
class ActionsAwakeMode:
    def enable():
        actions.app.notify("Talon is already awake")


@mod.action_class
class Actions:
    def talon_mode():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()

        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            if app.platform == "mac":
                actions.user.dragon_engine_sleep()
            elif app.platform == "windows":
                actions.user.dragon_engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.dragon_engine_command_mode()

    def playSound(file: str):
        """plays a sound to indicate wake up"""
        try:
            player.play(file)
        except:
            player.play('user/talon_sounds/1778__junggle__ambient-buttons/29150__junggle__btn340.wav')


    def sound_enable():
        """audio signal for enabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29065__junggle__btn255.wav')

    def sound_disable():
        """audio signal for disabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29035__junggle__btn225.wav')

    def sound_already_disabled():
        """audio signal for disabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29180__junggle__btn370.wav')

    def enable_withSound():
        """ensables the speech engine with a sound"""
        actions.speech.enable()
        actions.user.sound_enable()

    def disable_withSound():
        """disables the speech engine with a sound"""
        actions.user.sound_disable()
        actions.speech.disable()

    def dragon_mode():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            if app.platform == "mac":
                actions.user.dragon_engine_wake()
            elif app.platform == "windows":
                actions.user.dragon_engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.dragon_engine_normal_mode()
