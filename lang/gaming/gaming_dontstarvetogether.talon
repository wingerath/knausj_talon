mode: user.gaming_DontStarveTogether
mode: command 
and code.language: gaming_DontStarveTogether
-

settings():
    key_hold = 16.0
    key_wait = 20.0
    speech.timeout = 0.100
#    speech.engine = 'wav2letter'


(chirp): speech.enable()

abort: user.abort_action()

pick up:
    user.abort_action()
    key("shift:down")

attack:
    user.abort_action()
    key("ctrl:down f:down")

#active language: "gaming (Don't Starve Together)"


