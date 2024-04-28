import os
import azure.cognitiveservices.speech as speechsdk

key = os.environ.get('SPEECH_KEY')
region = os.environ.get('SPEECH_REGION')

speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = "hey"


def viseme_cb(evt):
    print("Viseme event received: audio offset: {}ms, viseme id: {}.".format(
        evt.audio_offset / 10000, evt.viseme_id))


speech_synthesizer.viseme_received.connect(viseme_cb)

result = speech_synthesizer.speak_text(text)
