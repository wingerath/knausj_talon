title:/Action Henk/
mode: sleep
-

tag(): user.gaming_ActionHenk
tag(): user.gaming

settings():
    key_hold = 32.0
    key_wait = 20.0
    speech.timeout = 0.150

try again: key(enter)
restart level: key(r)

# hook shot
parrot(tut):
  key(space:down)
  sleep(200ms)
  key(space:up)
parrot(trill): key("down")
parrot(click): mouse_click(0)
parrot(pop): mouse_click(2)


