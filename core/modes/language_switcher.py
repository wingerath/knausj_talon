from talon import Context, Module, settings, actions, app


mod = Module()
ctx = Context()


@mod.action_class
class Actions:

    def disable_german():
        """Set the language to english"""
        oldEngine = ctx.settings
        print(oldEngine)
        ctx.settings = {
            'speech.engine': 'wav2letter-conformer'
        }

    def enable_german():
        """Set the language to german"""
        oldEngine = ctx.settings
        print(oldEngine)
        ctx.settings = {
            'speech.engine': 'dragon'
        }

