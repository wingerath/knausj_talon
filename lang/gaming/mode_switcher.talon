#defines the various mode commands
mode: all
-
iris interact enable: user.eye_tracking_vision_enable()
iris cursor toggle: user.toggle_eye_tracking_cursor()
iris vision toggle: user.eye_tracking_vision_toggle()

face mode toggle: user.toggle_face_mode()
face mode normal: user.set_facial_mode("Talon")
face mode action henk: user.set_facial_mode("gaming_ActionHenk")
face mode don't starve together: user.set_facial_mode("gaming_DontStarveTogether")
face mode speed runners: user.set_facial_mode("gaming_SpeedRunners")
face mode among us: user.set_facial_mode("gaming_AmongUs")
face mode G T A for: user.set_facial_mode("gaming_gta4")
face mode unreal tournament: user.set_facial_mode("gaming_UnrealTournament")
face mode wolfenstein: user.set_facial_mode("gaming_wolfenstein")
face mode dragonball: user.set_facial_mode("gaming_dragonball")
face mode trackmania: user.set_facial_mode("gaming_trackmania")
face mode batman: user.set_facial_mode("gaming_BatmanArkhamCity")

#discord toggle: key("ctrl-shift-m")

game toggle:
  key("alt-1")
  key("f8")

toggle aim:
  key("f4")
  key("f8")
