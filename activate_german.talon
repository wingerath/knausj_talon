mode: command
-
^german$:
	  mode.enable("user.german")
    key("ctrl-shift-alt-+")
    user.sound_enable()


^english$: skip()
