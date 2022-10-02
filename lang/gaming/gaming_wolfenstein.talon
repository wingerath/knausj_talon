title:/Wolfenstein/
mode: sleep
-

tag(): user.gaming
tag(): user.gaming_UnrealTournament

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



