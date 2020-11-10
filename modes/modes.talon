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
# begin: these commands are really for windows & mac with Dragon.
go to sleep:
    key("keypad_divide") #Dragon hotkey
talon sleep: speech.disable()
talon wake: speech.enable()
dragon mode: user.dragon_mode()
dragon run <user.text>: user.engine_mimic("{text}")
talon mode: user.talon_mode()
# end: these commands are really for windows & mac on Dragon.
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command and dictation mode$:
    mode.disable("sleep")
    mode.enable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
