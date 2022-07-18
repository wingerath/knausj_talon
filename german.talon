language: de_DE
-

^(englisch)$:
    key("ctrl-shift-alt-+")
	  mode.disable("user.german")
  	mode.disable("user.german_conformer")
    user.sound_enable()

^(snore)$:
    key("ctrl-shift-alt-+")
	  mode.disable("user.german")
    speech.disable()
    user.sound_disable()

^microphone off$:
    user.engine_mimic("Mikrofon ausschalten")
	  mode.disable("user.german")
  	mode.disable("user.german_conformer")
    user.microphone_select_none()
    user.sound_disable()

talon sleep | snore | go to sleep: skip()

#<phrase>: insert(user.formatted_text("{phrase}", 'DRAGON_TEXT'))

Umbruch: key("shift-enter")


