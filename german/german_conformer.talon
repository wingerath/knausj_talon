language: de_DE
mode: user.german_conformer
-

^(englisch)$:
  	mode.disable("user.german_conformer")
    user.sound_enable()

^(snore)$:
    speech.disable()
    user.sound_disable()

^microphone off$:
  	mode.disable("user.german_conformer")
    user.microphone_select_none()
    user.sound_disable()

