language: de_DE
-

^(englisch)$:
    key("ctrl-shift-alt-+")
	  mode.disable("user.german")
    user.sound_enable()

^(snore)$:
    key("ctrl-shift-alt-+")
	  mode.disable("user.german")
    speech.disable()
    user.sound_disable()

^microphone off$:
    user.engine_mimic("Mikrofon ausschalten")
	  mode.disable("user.german")
  	mode.disable("user.de_DE")
    user.microphone_select_none()
    user.sound_disable()

talon sleep | snore | go to sleep: skip()


Umbruch: key("shift-enter")


