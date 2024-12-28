title:/Parsec/
mode: sleep
-
tag(): user.gaming
tag(): user.gaming_mgs55



^other window$: key("alt-tab")
^(escape | exit)$: user.hold_button("escape", 100, true)
^kill$: user.hold_button("backspace", 100, true)
^enter$: user.hold_button("enter", 100, true)
^map$: user.hold_button("m", 100, true)


parrot(blup): user.hold_button("x", 100, true)
parrot(pop): user.hold_button("x", 100, true)
parrot(click): user.hold_button("x", 100, true)
nparrot(click): user.hold_button("x", 100, true)
parrot(tut): user.hold_button("x", 100, true)

########################
# PlayStation Controls #
########################
# Reference: https://metalgear.fandom.com/wiki/Metal_Gear_Solid_V:_Ground_Zeroes/Controls


###############
# PC Controls #
###############
# Got it from chat get and the following link:
# https://steamcommunity.com/sharedfiles/filedetails/?id=902543330


# Change stance. Press once to get in a crouched position
(stance): user.hold_button("ctrl", 100, true)

# Action (Climb, Pick Locks, etc.)
^(each | action)$: user.hold_button("e", 100, true)

# Reload Weapon/Carry
^(red | reload)$: user.hold_button("r", 100, true)

# Quick Dive
^(space | dive)$: user.hold_button("space", 100, true)

# Move Character (WASD)
#^(move forward)$: user.hold_button("w", 100, true)
#^(move backward)$: user.hold_button("s", 100, true)
#^(move left)$: user.hold_button("a", 100, true)
#^(move right)$: user.hold_button("d", 100, true)

# Sprint (Hold Shift)
^(run)$: key("shift:down")
stand:
  key("shift:up")
  key("ctrl:up")

# Move Camera/Aim Weapon
#^(aim)$: user.hold_button("right_mouse_button", 100, true)
# Aim Weapon (Hold Right Mouse Button)
^target on$: user.hold_button("ö", 12000, false)
^target off$: user.push_button("ö", "down")

# Equip Items and Weapons
^equip <number_small>$: user.hold_button("{number}", 100, true)

# Radio
^(quick | radio)$: user.hold_button("q", 100, true)

# Switch Aiming Sides (While aiming)
^(switch aim)$: user.hold_button("shift", 100, true)

# Zoom with Binoculars
# Zoom into First-Person View (While aiming)
^(zoom in)$: user.mouse_scroll_down()
^(zoom out)$: user.mouse_scroll_up()

# Binoculars
^(bat | binoculars)$: user.hold_button("b", 100, true)

# Fire/Throw weapon or item (While aiming)
#^(fire | throw)$: user.hold_button("left_mouse_button", 100, true)

# Open the iDroid
^(tab | open idroid)$: user.hold_button("tab", 100, true)
#^tabber$: key("tab:down")
