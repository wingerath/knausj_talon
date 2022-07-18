not mode: sleep
-
talon sleep | snore | go to sleep:
    speech.disable()
    user.sound_disable()
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
dragon run <user.text>: user.engine_mimic("{text}")
