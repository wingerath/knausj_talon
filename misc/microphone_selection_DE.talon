mode: user.german
language: de_DE
-
^Microphone off$:
    user.microphone_select_none()
    user.engine_mimic("Mikrofon ausschalten")
	mode.disable("user.german")
    user.sound_disable()
