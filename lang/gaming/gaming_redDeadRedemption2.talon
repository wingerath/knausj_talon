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


<user.ordinals>: core.repeat_command(ordinals-1)
on foot mode: user.set_mode("on_foot")
default mode: user.set_mode("default")

other window: key("alt-tab")
(escape | exit): key("escape")
kill: key("backspace")
enter: user.hold_button("enter", 100, true)
map: user.hold_button("m", 100, true)
sit: user.hold_button("i", 200, true)
bat: user.hold_button("b", 200, true)
fine: user.hold_button("f", 100, true)
quick: user.hold_button("q", 200, true)
vest: user.hold_button("v", 200, true)
target: user.hold_button("ö", 1000, false)
target on: user.hold_button("ö", 12000, false)
target off: user.push_button("ö", "down")
tabber: key("tab:down")

jump: user.hold_button("space", 100, true)
eagle: user.hold_button("ß", 100, true)
parrot(pop): user.hold_button("ä", 500, true)
punch: user.hold_button("ä", 500, true)
parrot(tut): user.hold_button("h", 100, true)
harp: user.hold_button("h", 100, true)
#parrot(click): user.hold_button("f", 50)
#parrot(trill): user.hold_button("w", 1000, true)

# noise controls
#parrot(blup): key("f")
parrot(pop): key("f")
#parrot(click): mouse_click(1)
#parrot(tut):
#parrot(trill): key("f")
#parrot(click): key("ö")
#parrot(tut): key("ö")
#parrot(pop): mouse_click(2)

duck: key("ctrl:down")
run: key("shift:down")
stand:
  key("ctrl:up")
  key("shift:up")
