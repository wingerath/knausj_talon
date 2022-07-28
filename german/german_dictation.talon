language: de_DE
-

Leertaste: insert(' ')
Gänsefüßchen: insert('"')
Bindestrich: insert('-')
Unterstrich: insert('_')
Raute: insert('#')
Schrägstrich: insert("/")
Backslash: insert("\\")
Apostroph: insert("'")
Klammer: insert("(")
Asterisk: insert("*")
at: insert("@")
Innen: "Innen"

Absatz: key("enter:2")
Umbruch: key("shift-enter")
enter: key("enter")
tab: key("tab")
shift tab: key("tab")


<phrase>: insert(user.formatted_text("{phrase}", 'DRAGON_TEXT'))
groß <phrase>: insert(user.formatted_text(user.formatted_text("{phrase}", "CAPITALIZE_FIRST_WORD"), "DRAGON_TEXT"))
Kleinbuchstaben <phrase>: insert(user.formatted_text(user.formatted_text("{phrase}", "LOWERCASE_FIRST_WORD"), "DRAGON_TEXT"))
öffne Diktierfenster: key(ctrl-shift-d)

(left | links): key("left")
(right | rechts): key("right")
