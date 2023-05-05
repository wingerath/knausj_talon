app:Microsoft PowerPoint
mode: command
-
slide:
  key("alt-r")
  key("ä n")
  key("down")
  key("right:5")
  key("enter")
  key("down")
  sleep(500ms)


move:
  user.engine_mimic("touch")
  key("ctrl-a")
  key("ctrl-c")
  key("pagedown")
  key("alt-r")
  key("v 1")
  key("u")
  key("pagedown")
  sleep(1000ms)

fix:
  user.engine_mimic("touch")
  sleep(100ms)
  key("ctrl-a shift-left")
  sleep(100ms)
  key("ctrl-x")
  sleep(100ms)
  key("escape")
  sleep(100ms)
  key("delete")
  sleep(100ms)
  user.engine_mimic("touch")
  sleep(100ms)
  key("alt-r")
  key("v 1")
  sleep(100ms)
  key("t")
  sleep(100ms)
  key("pagedown:2")
  sleep(500ms)

clean:
  key("delete down")
  sleep(500ms)

kicker:
  user.engine_mimic("touch")
  sleep(200ms)
  key("delete")
  sleep(200ms)
  key("pagedown")
  sleep(200ms)

animate:
  key("alt-v")
  key("n")
  key("down")
  key("right")
  key("enter")

align left:
  key("alt-r")
  key("g")
  key("h")
  key("l")

align right:
  key("alt-r")
  key("g")
  key("h")
  key("r")

align top:
  key("alt-r")
  key("g")
  key("h")
  key("b")

align bottom:
  key("alt-r")
  key("g")
  key("h")
  key("n")

align center:
  key("alt-r")
  key("g")
  key("h")
  key("i")

align middle:
  key("alt-r")
  key("g")
  key("h")
  key("k")
