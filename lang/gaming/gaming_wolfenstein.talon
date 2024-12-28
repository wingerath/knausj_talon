app: WolfNewOrder
mode: sleep
-

tag(): user.gaming
tag(): user.gaming_wolfenstein

settings():
    key_hold = 150.0
    key_wait = 20.0

<user.ordinals>: core.repeat_command(ordinals-1)

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

sprint:
    key("shift:down")
    sleep(100ms)
    key("shift:up")

stand up:
    key("ctrl:up")
    key("shift:up")

each | use: key("e")
pix | dual wield | double: key("x")
golf | grenade: key("g")
mike | map: key("m")
june | journal: key("j")
red | reload: key("r")
odd | throw | knife: key("o")
n | next | next weapon: key("n")

parrot(pop): key("ß")
parrot(tut): key("ß")
aim | target on:
   user.push_button("ö", "up")
   user.hold_button("ö", 12000, false)
target off: user.push_button("ö", "up")
"item <number>": key("{number}")
enter: key("enter")
escape: key("escape")

other window: key("alt-tab")

