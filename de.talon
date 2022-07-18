language: de_DE
-
englisch bitte: print("english please")
sag <phrase>: insert(user.formatted_text("{phrase}", "NOOP"))



^(english)$: mode.disable("user.de_DE")

