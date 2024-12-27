mode: command
-
^german$:
	mode.enable("user.german")
    key("ctrl-shift-alt-+")
    user.sound_enable()


^german conformer: mode.enable("user.german_conformer")

^english$: skip()
