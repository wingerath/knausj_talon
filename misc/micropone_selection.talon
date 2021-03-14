^microphone show$: user.microphone_selection_toggle()
^microphone pick <number_small>$: user.microphone_select(number_small)
^microphone off$:
    speech.disable()
    user.microphone_select_none()
