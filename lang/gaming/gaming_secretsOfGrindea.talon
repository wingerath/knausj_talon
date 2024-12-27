title: Secrets of Grindea
mode: sleep
-

tag(): user.gaming
tag(): user.gaming_secretsOfGrindea

settings():
    key_hold = 16.0
    key_wait = 20.0
    speech.timeout = 0.100
#    speech.engine = 'wav2letter'


# noise controls
#parrot(blup):
#	key(shift)
#parrot(pop): mouse_click(0)
parrot(tut): user.hold_button("2", 500, true)
parrot(pop): user.hold_button("4", 500, true)
#	key(shift)

(chirp): speech.enable()

abort: user.abort_action()

pick up:
    user.abort_action()
    key("shift:down")

attack:
    user.abort_action()
    key("ctrl:down")

#active language: "gaming (Don't Starve Together)"

menu: key(escape)
booker: key(c)
speller: key(v)
inventory: key(i)
^item <number>$: key("{number}")


drag:
	user.mouse_drag(0)
end drag | drag end:
    user.mouse_drag_end()
