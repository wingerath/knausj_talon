title:/DRAGON BALL/
mode: sleep
-

tag(): user.gaming

settings():
    key_hold = 32.0
    key_wait = 20.0
    speech.timeout = 0.150
#    speech.engine = 'wav2letter'

(bat | roll): key("b")
(fine | boost): key("f")


one: key("1")
two: key("2")
three: key("3")
(for | four): key("4")
five: key("5")
six: key("6")
seven: key("7")
eight: key("8")
nine: key("9")
zero: key("0")


parrot(motorboat): user.hold_button("ctrl")
parrot(click): mouse_click(0)
parrot(pop): mouse_click(1)
parrot(tut): mouse_click(2)
parrot(broken_saxophone): user.hold_button("alt")

parrot(ch_bach):
	print("ch_bach")
#	key("xxx")

parrot(uboat):
	print("uboat")
#	key("xxx")


