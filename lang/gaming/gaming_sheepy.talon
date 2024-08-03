title:SheepyAShortAdventure
mode: sleep
-
tag(): user.gaming
tag(): user.gaming_sheepy

settings():
#    key_hold = 96.0
#    key_wait = 20.0
#    speech.timeout = 0.150
#    speech.engine = 'wav2letter'

^start the game now$:
  key("alt:down")
  key("f2:down")
  sleep(100ms)
  key("alt:up")
  key("f2:up")
  key("enter")
  key("alt:down")
  key("f1:down")
  sleep(100ms)
  key("alt:up")
  key("f1:up")

<user.ordinals>: core.repeat_command(ordinals-1)

other window: key("alt-tab")
escape: key("escape")
enter: key("enter")

# noise controls
#parrot(blup): key("f")
#parrot(pop): key("f")
parrot(click): key("shift")
parrot(tut): key("ctrl")
#parrot(tut):
#parrot(trill): key("f")
#parrot(click): key("ö")
#parrot(tut): key("ö")
#parrot(pop): mouse_click(2)
