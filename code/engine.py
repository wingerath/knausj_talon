from talon import Context, Module
from talon import speech_system

mod = Module()


@mod.action_class
class Actions:
    def engine_sleep():
        """Sleep the engine"""
        speech_system.engine_mimic("go to sleep"),

    def engine_wake():
        """Wake the engine"""
        speech_system.engine_mimic("wake up"),

    def engine_dictation_mode():
        """Wake the engine"""
        speech_system.engine_mimic("switch to dictation mode"),

    def engine_command_mode():
        """Wake the engine"""
        speech_system.engine_mimic("switch to command mode"),

    def engine_dictation_and_commands_mode():
        """Wake the engine"""
        speech_system.engine_mimic("switch to dictation and commands mode"),

    def engine_mimic(cmd: str):
        """Sends phrase to engine"""
        speech_system.engine_mimic(cmd)
