from talon import actions, app

def on_ready():
    actions.user.microphone_select_none()
app.register('launch', on_ready)
