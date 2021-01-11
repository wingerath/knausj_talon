mode: user.gaming_Wolfenstein
mode: command 
and code.language: gaming_Wolfenstein
-

settings():
    key_hold = 150.0
    key_wait = 20.0

Sprint slide:
    key("b:down")
    sleep(100ms)
    key("ctrl:down")
    sleep(100ms)
    key("b:up")
    key("ctrl:up")

Crouch:
    key("ctrl:down")
    sleep(100ms)
    key("ctrl:up")

active language: "gaming (Wolfenstein)"

