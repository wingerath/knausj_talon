title:GTAIV
mode: sleep
-

tag(): user.gaming
tag(): user.gaming_gta4

settings():
    key_hold = 32.0
    key_wait = 20.0
    speech.timeout = 0.150
#    speech.engine = 'wav2letter'

stun: key("q")

stunner:
  key("q")
  sleep(500ms)
  key("q")
  sleep(500ms)
  key("q")

# noise controls
#parrot(blup):
#	key(shift)
#parrot(pop):
#	mouse_click(1)
#parrot(tut):
#	key(shift)

each: key("e")
quick: key("q")
red: key("r")
trap: key("t")
yank: key("y")
pix: key("x")
fine: key("f")
odd: key("o")

mick: mouse_click(2)

duck: key("ctrl:down")
run: key("space:down")
stand:
  key("ctrl:up")
  key("space:up")


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


claw:
  key("2")
  sleep(100ms)
  key("2")



parrot(trill): key("f")
parrot(click): mouse_click(0)
parrot(pop): mouse_click(2)

#parrot(trill): mouse_click(0)
parrot(broken_saxophone):
  key("ctrl:down")
  sleep(100ms)
  key("ctrl:up")

parrot(ch_bach):
	print("ch_bach")
#	key("xxx")

parrot(uboat):
	print("uboat")
#	key("xxx")


toggle touch: user.toggle_mouse_button(0)
toggle rick: user.toggle_mouse_button(1)
toggle mike: user.toggle_mouse_button(2)

