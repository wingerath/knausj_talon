from talon import Context, Module

ctx = Context()
mod = Module()
apps = mod.apps
apps.slack = "app.name: Slack"
apps.slack = """
os: windows
and app.name: slack.exe
"""

mod.list("emoji", desc="Slack emojies")


@mod.capture
def emoji(m) -> str:
    "Slack emojies"


ctx.lists["user.emoji"] = {
    "muscle": ":muscle:",
    "scream": ":scream:",
    "smile tears": ":joy:",
    "smile": ":smile:",
    "smile sweat": ":sweat_smile:",
    "thumbs up": ":thumbsup:",
    "year boy": ":yeboi:",
}


@ctx.capture(rule="{user.emoji}")
def emoji(m):
    return m.emoji
