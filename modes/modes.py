from talon import Module, actions, app, speech_system, Context
import sounddevice as sd
import soundfile as sf
import threading
import queue

mod = Module()

class SoundPlayer:
    def __init__(self):
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._play_sound_thread)
        self.thread.start()

    def _play_sound_thread(self):
        while True:
            filename = self.queue.get()
            if filename == 'exit':
                break
            data, samplerate = sf.read(filename, dtype='float32')
            sd.play(data, samplerate)
            sd.wait()

    def play(self, filename):
        self.queue.put(filename)

    def stop(self):
        self.queue.put('exit')
        self.thread.join()

player = SoundPlayer()


modes = {
    "admin": "enable extra administration commands terminal (docker, etc)",
    "debug": "a way to force debugger commands to be loaded",
    "gdb": "a way to force gdb commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
    "windbg": "a way to force windbg commands to be loaded",

    "german": "german language",
    "german_conformer": "german language with conformer",
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
            player.play(file)
        except:
            player.play('user/talon_sounds/1778__junggle__ambient-buttons/29150__junggle__btn340.wav')

    def sound_enable():
        """audio signal for enabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29065__junggle__btn255.wav')

    def sound_disable():
        """audio signal for disabling speech"""
        actions.user.playSound('user/talon_sounds/1778__junggle__ambient-buttons/29035__junggle__btn225.wav')

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
                actions.user.engine_wake()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("start normal mode")
