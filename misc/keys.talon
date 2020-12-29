go <user.arrow_keys>: key(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]: 
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")


# hold and release modifiers
hold <user.modifiers>: key("{modifiers}:down")
release <user.modifiers>: key("{modifiers}:up")

<user.modifiers> space: key("{modifiers}-space")
(number | num) <user.number_key>: key("keypad_{number_key}")
(number | num) <user.key>: key("keypad_{key}")
#if number < 10:
#    actions.key("ctrl-keypad_{}".format(number))