language: de_DE
-

^(englisch)$:
    key("ctrl-shift-alt-+")
    user.disable_german()
    user.sound_enable()

^(snore)$:
    key("ctrl-shift-alt-+")
    user.disable_german()
    speech.disable()
    user.sound_disable()

^(microphone off | Microphone auf)$:
    user.disable_german()
    user.microphone_select_none()
    user.engine_mimic("Mikrofon ausschalten")
    user.sound_disable()

^(german | Chairman)$: skip()


Umbruch: key("shift-enter")


