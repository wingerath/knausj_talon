mode: sleep
-
settings():
    #stop continuous scroll/gaze scroll with a pop
    user.mouse_enable_pop_stops_scroll = 0
	#enable pop click with 'control mouse' mode
	user.mouse_enable_pop_click = 0

#this exists solely to prevent talon from walking up super easily in sleep mode at the moment with wav2letter
<phrase>: skip()

^(chirp)$:
    speech.enable()
    user.sound_enable()

^snore$:
    user.sound_already_disabled()

^chirp german$:
    user.engine_mimic("chirp")
#    sleep(.05)
    user.engine_mimic("german")


^microphone off$:
    user.microphone_select_none()
    speech.enable()
    user.sound_disable()

