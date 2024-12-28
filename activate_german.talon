mode: command
-
^german$:
    key("ctrl-shift-alt-+")
    user.enable_german()
    user.sound_enable()


^german conformer: mode.enable("user.german_conformer")

^english$: skip()

