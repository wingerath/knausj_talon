from talon import Module

mod = Module()
apps = mod.apps
apps.slack = "app.name: Slack"
apps.slack = "app.name: Slack.exe"
apps.slack = "app.name: slack.exe"

mod.list("emoji", desc="Slack emojies")


@mod.capture
def emoji(m) -> str:
    "Slack emojies"


ctx.lists["user.emoji"] = {
    "smile tears": ":joy:",
    "smile": ":smile:",
    "sweat smile": ":sweat_smile:",
    "year boy": ":yeboi:",
}


@ctx.capture(rule="{user.emoji}")
def emoji(m):
    return m.emoji
