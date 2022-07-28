^microphone show$: user.microphone_selection_toggle()
^microphone close$: user.microphone_selection_hide()
^microphone pick <number_small>$: user.microphone_select(number_small)
^microphone off$:
	  mode.enable("user.german")
    user.microphone_select_none()
    user.engine_mimic("Mikrofon ausschalten")
	  mode.disable("user.german")
    user.sound_disable()
