from talon import speech_system, Context, actions
from talon.engines.w2l import W2lEngine
from talon.engines.vosk import VoskEngine
w2l = W2lEngine(model='en_US', debug=False)
vosk_de = VoskEngine(model='vosk-model-de-0.6', language='de_DE')
speech_system.add_engine(w2l)
speech_system.add_engine(vosk_de)


# # ideally you integrate this into your engines.py file
#1
# from talon import speech_system, Context
#
#
# # especially this should not be here but in your engines.py file:
ctx = Context()
ctx.settings = {
    'speech.engine': 'wav2letter', # your default engine goes here
    'speech.engine': 'dragon', # your default engine goes here
}