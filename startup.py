from talon import actions, app

def on_ready_wolle():
    actions.user.microphone_select_none()
    actions.user.hud_add_single_click_mic_toggle()
    actions.user.hud_toolkit_scope()
app.register('launch', on_ready_wolle)
