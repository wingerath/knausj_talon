mode: user.german_conformer
language: de_DE
-
settings():
    speech.language = 'de_DE'
#    speech.engine = 'dragon'


^(englisch)$:
  	mode.disable("user.german_conformer")
    user.sound_enable()

^(snore)$:
  	mode.disable("user.german_conformer")
    speech.disable()
    user.sound_disable()

^microphone off$:
  	mode.disable("user.german_conformer")
    user.microphone_select_none()
    user.sound_disable()


<phrase>: insert(user.formatted_text("{phrase}", 'DRAGON_TEXT'))
