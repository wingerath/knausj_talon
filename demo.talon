mode: sleep
-

#face(smile): key(x)

#face(brow_down_left): print(brow_down_left)
#face(brow_down_right): print(brow_down_right)
#face(brow_inner_up): print(brow_inner_up)
#face(brow_outer_up_left): print(brow_outer_up_left)
#face(brow_outer_up_right): print(brow_outer_up_right)
#face(blink_left): print(blink_left)
#face(blink_right): print(blink_right)
#face(gaze_down_left): print(gaze_down_left)
#face(gaze_down_right): print(gaze_down_right)
#face(gaze_in_left): print(gaze_in_left)
#face(gaze_in_right): print(gaze_in_right)
#face(gaze_out_left): print(gaze_out_left)
#face(gaze_out_right): print(gaze_out_right)
#face(gaze_up_left): print(gaze_up_left)
#face(gaze_up_right): print(gaze_up_right)
#face(squint_left): print(squint_left)
#face(squint_right): print(squint_right)
#face(eye_wide_left): print(eye_wide_left)
#face(eye_wide_right): print(eye_wide_right)
#face(jaw_open): print(jaw_open)
#face(jaw_left): print(jaw_left)
#face(jaw_right): print(jaw_right)
#face(mouth_close): print(mouth_close)
#face(dimple_left): print(dimple_left)
#face(dimple_right): print(dimple_right)
#face(frown_left): print(frown_left)
#face(frown_right): print(frown_right)
#face(mouth_funnel): print(mouth_funnel)
#face(mouth_lower_down_left): print(mouth_lower_down_left)
#face(mouth_lower_down_right): print(mouth_lower_down_right)
#face(mouth_press_left): print(mouth_press_left)
#face(mouth_press_right): print(mouth_press_right)
#face(mouth_pucker): print(mouth_pucker)
#face(mouth_right): print(mouth_right)
#face(mouth_left): print(mouth_left)
#face(mouth_roll_lower): print(mouth_roll_lower)
#face(mouth_roll_upper): print(mouth_roll_upper)
#face(mouth_shrug_lower): print(mouth_shrug_lower)
#face(mouth_shrug_upper): print(mouth_shrug_upper)
#face(smile_left): print(smile_left)
#face(smile_right): print(smile_right)
#face(mouth_stretch_left): print(mouth_stretch_left)
#face(mouth_stretch_right): print(mouth_stretch_right)
#face(mouth_upper_up_left): print(mouth_upper_up_left)
#face(mouth_upper_up_right): print(mouth_upper_up_right)

mouse movement test: user.mouse_move(50, -50)


#font:
  user.engine_mimic("touch")
  sleep(500ms)
  key(ctrl-a)
  sleep(500ms)
  key(alt-r)
  key(s c)
  sleep(500ms)
  "Arial"
  key(enter)
  sleep(500ms)
  key("pagedown")
  sleep(500ms)

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
