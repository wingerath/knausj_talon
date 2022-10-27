title:Among Us
mode: sleep
-

tag(): user.gaming
tag(): user.gaming_AmongUs

settings():
    key_hold = 16.0
    key_wait = 20.0
    speech.timeout = 0.100
#    speech.engine = 'wav2letter'

(escape | cancel): key("escape")
(map | tab): key("tab")
(vent | vest): key("v")
(interact | do | each): key("e")
#parrot(pop): key("e")
(kill | quench): key("q")
#parrot(tut): key("q")
(report | phone | red): key("r")
(move | roll ability | fine): key("f")


parrot(pop): mouse_click(1)
