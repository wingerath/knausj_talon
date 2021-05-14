#defines the various mode commands
mode: all
-
welcome back:
    user.mouse_wake()
    user.history_enable()
    user.talon_mode()
sleep all:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
talon sleep | snore | go to sleep: speech.disable()
(please wake up you son of a gun you):
    speech.enable()
dragon sleep:
    speech.disable()
    user.engine_sleep()
    speech.enable()
# begin: these commands are really for windows & mac with Dragon.
dragon mode: user.dragon_mode()
dragon run <user.text>: user.engine_mimic("{text}")
dragon activate: user.engine_dictation_and_commands_mode()
talon mode: user.talon_mode()
# end: these commands are really for windows & mac on Dragon.
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
    user.engine_command_mode()
^command and dictation mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
    user.engine_command_mode()
^command and dragon mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    user.engine_dictation_and_commands_mode()
