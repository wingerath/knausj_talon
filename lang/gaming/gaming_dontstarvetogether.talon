title:/Don't Starve Together/
mode: sleep
-

settings():
    key_hold = 16.0
    key_wait = 20.0
    speech.timeout = 0.100
#    speech.engine = 'wav2letter'


# noise controls
#parrot(blup):
#	key(shift)
parrot(pop):
	mouse_click(1)
parrot(tut):
	key(shift)

(chirp): speech.enable()

abort: user.abort_action()

pick up:
    user.abort_action()
    key("shift:down")

attack:
    user.abort_action()
    key("ctrl:down")

#active language: "gaming (Don't Starve Together)"


