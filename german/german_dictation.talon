language: de_DE
and not app: /Dragon for Windows/
and not title: /LibreOffice Calc/
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
Pluszeichen: insert("+")
at: insert("@")
Innen: "Innen"

Absatz: key("enter:2")
Umbruch: key("shift-enter")
enter: key("enter")
tab: key("tab")
shift tab: key("tab")
Punkt [Leertaste] <phrase>:
  insert(". ")
  insert(user.formatted_text(user.formatted_text("{phrase}", "CAPITALIZE_FIRST_WORD"), "DRAGON_TEXT"))
Ausrufezeichen [Leertaste] <phrase>:
  insert("! ")
  insert(user.formatted_text(user.formatted_text("{phrase}", "CAPITALIZE_FIRST_WORD"), "DRAGON_TEXT"))
Fragezeichen [Leertaste] <phrase>:
  insert("? ")
  insert(user.formatted_text(user.formatted_text("{phrase}", "CAPITALIZE_FIRST_WORD"), "DRAGON_TEXT"))

<phrase>: insert(user.formatted_text("{phrase}", 'DRAGON_TEXT'))
groß <phrase>: insert(user.formatted_text(user.formatted_text("{phrase}", "CAPITALIZE_FIRST_WORD"), "DRAGON_TEXT"))
Kleinbuchstaben <phrase>: insert(user.formatted_text(user.formatted_text("{phrase}", "LOWERCASE_FIRST_WORD"), "DRAGON_TEXT"))
öffne Diktierfenster: key(ctrl-shift-d)

go left: key("left")
(go right | go reit): key("right")

Klammer auf: "("
Klammer zu: ")"

null: "0"
eins: "1"
zwei: "2"
drei: "3"
vier: "4"
fünf: "5"
sechs: "6"
sieben: "7"
acht: "8"
neun: "9"
zehn: "10"
elf: "11"
zwölf: "12"
zwei tausend achtzehn: "2018"
zwei tausend neunzehn: "2019"
zwei tausend zwanzig: "2020"
zwei tausend einundzwanzig: "2021"
zwei tausend zweiundzwanzig: "2022"
