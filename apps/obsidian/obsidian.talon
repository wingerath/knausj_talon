language: de_DE
language: en_US
app: obsidian
-

Entity: key(ctrl-alt-8:2)

neuer Tag:
  key("ctrl-shift-p")
  sleep(100ms)
  key("ctrl-shift-u")
  sleep(100ms)
  key("ctrl-m")
  sleep(500ms)
  insert("Daily Notes")
  key("enter")
  sleep(100ms)
  key("ctrl-shift-p")

Ordner Link:
  insert("[Ordner](<>)")
  key("left:2")

Web Link:
  insert("[Webseite]()")
  key("left")

Bild einfügen:
  insert("![[]]")
  key("left:2")

Schmaler machen:
  key("left:2")
  insert("|200")

(left | links): key("left")
(right | rechts): key("right")





