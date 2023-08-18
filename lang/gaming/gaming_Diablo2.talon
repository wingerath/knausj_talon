title:Diablo II: Resurrected
mode: sleep
-
tag(): user.gaming
tag(): user.gaming_Diablo2

settings():
    key_hold = 32.0
    key_wait = 32.0
    speech.timeout = 0.100


tab: key(tab)
escape: key(escape)
#air: key(a)
#drum: key(d)

wale: key(w)
trap: key(t)
odd: key(o)
golf: key(g)
quick: key(q)
sit: key(i)

town: key(f8)
scroll: key(f7)
shield: key(f5)

one: key(1)
two: key(2)
three: key(3)
four: key(4)

(call to arms | buffer):
  key(w)
  sleep(500ms)
  key(f1)
  sleep(800ms)
  key(f2)
  sleep(800ms)
  key(w)
  sleep(800ms)
  key(f5)

parrot(pop): mouse_click(0)

