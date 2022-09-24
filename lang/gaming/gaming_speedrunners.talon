title:/SpeedRunners/
mode: sleep
-

tag(): user.SpeedRunners

settings():
    key_hold = 32.0
    key_wait = 20.0
    speech.timeout = 0.150
#    speech.engine = 'wav2letter'

parrot(trill): key("c")
parrot(broken_saxophone): key("x")
parrot(click): key("x")
parrot(tut): key("a")
parrot(pop): key("c")
parrot(broken_saxophone): key("z")




zip: key("z")
escape: key("escape")
plex: key("x")
(cam | fire): key("c")
(space | boost): key("space")
(trap | taunt): key("t")
(fine | swap | weapon): key("f")
(tab | player info): key("tab")

down:
  key("down:down")
  sleep(100ms)
  key("down:up")
parrot(tut):
  key("right:up")
  key("left:down")
parrot(click):
  key("left:up")
  key("right:down")
stop:
  key("left:up")
  key("right:up")
