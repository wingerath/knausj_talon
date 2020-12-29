mode: user.gaming
mode: command 
and code.language: gaming
-


settings():
    key_hold = 16.0
    key_wait = 8.0
    key_wait = 1.0

Sprint slide:
    key("b:down")
    sleep(100ms)
    key("ctrl:down")
    sleep(100ms)
    key("b:up")
    key("ctrl:up")

attack:
    key("f:down")
    sleep(100ms)
    key("f:up")
    sleep(100ms)

Crouch:
    key("ctrl:down")
    sleep(100ms)
    key("ctrl:up")

active language: "gaming mode is working"

