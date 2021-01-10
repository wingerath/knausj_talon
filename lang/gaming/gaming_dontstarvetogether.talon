mode: user.gamingdontstarvetogether
mode: command 
and code.language: gamingdontstarvetogether
-

settings():
    key_hold = 150.0
    key_wait = 20.0
    speech.engine = 'wav2letter'

abort: user.abort_action()

pick up:
    user.abort_action()
    key("shift:down")

attack:
    user.abort_action()
    key("ctrl:down f:down")

active language: "gaming (Don't Starve Together)"

