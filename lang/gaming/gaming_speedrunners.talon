title:/SpeedRunners/
mode: sleep
-

tag(): user.gaming
tag(): user.gaming_SpeedRunners

settings():
    key_hold = 32.0
    key_wait = 20.0
    speech.timeout = 0.150
#    speech.engine = 'wav2letter'

#parrot(trill): user.hold_button("space")
#parrot(click): key("x")
#parrot(pop): key("c")
#parrot(click): key("z")




zip: key("z")
escape: key("escape")
plex: key("x")
(cam | fire): key("c")
(space | boost): key("space"z)
(trap | taunt): key("t")
(fine | swap | weapon): key("f")
(tab | player info): key("tab")

parrot(click): user.hold_button("down")
left:
  key("right:up")
  key("left:down")
  key("z:down")
  sleep(300ms)
  key("z:up")
right:
  key("left:up")
  key("right:down")
  key("z:down")
  sleep(300ms)
  key("z:up")
stop:
  key("left:up")
  key("right:up")
