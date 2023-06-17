mode: sleep
-

#font:
  user.engine_mimic("touch")
  sleep(200ms)
  key(ctrl-a)
  key(alt-r)
  key(s c)
  "Arial"
  key(enter)
  key("pagedown")
  sleep(200ms)

gamepad(left_xy:repeat):
    x = x * 20
    y = y * -60
    mouse_scroll(y, x)
gamepad(north): key(cmd-`)
gamepad(south): key(cmd-tab)
gamepad(r1:down): mouse_drag(0)
gamepad(r1:up):   mouse_release(0)
gamepad(l1:down): mouse_drag(1)
gamepad(l1:up):   mouse_release(1)

gamepad(right_xy:repeat):
    mx = mouse_x()
    my = mouse_y()
    x = x * 25
    y = y * 25
    mouse_move(mx + x, my - y)
