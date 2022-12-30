title:Red Dead Redemption 2
mode: sleep
-
tag(): user.gaming
tag(): user.gaming_redDeadRedemption2

settings():
    key_hold = 32.0
    key_wait = 20.0
    speech.timeout = 0.150
#    speech.engine = 'wav2letter'

tab: key("tab")
golf: key("g")
harp: key("h")
vest: key("v")
fine: key("f")
yank: key("y")
jump: key("space")
close steam: key("shift-tab")

red:
  key("r:down")
  sleep(700ms)
  key("r:up")

mission:
  key("alt:down")
  sleep(2000ms)
  key("alt:up")

each:
  key("e:down")
  sleep(500ms)
  key("e:up")

bat:
  key("b:down")
  sleep(700ms)
  key("b:up")

# noise controls
parrot(blup): key("f")
parrot(pop): key("f")
#parrot(click): mouse_click(1)
#parrot(tut):
#	key(shift)

(escape | exit): key("escape")
kill: key("backspace")
pix: key("x")
pit: key("p")
other window: key("alt-tab")

mick: mouse_click(2)

duck: key("ctrl:down")
run: key("shift:down")
stand:
  key("ctrl:up")
  key("shift:up")


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

parrot(trill): key("f")
parrot(click): key("ö")
parrot(tut): key("ö")
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

