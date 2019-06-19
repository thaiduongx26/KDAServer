from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import texttospeech

t2s = texttospeech.TextToSpeechClient()
client = speech.SpeechClient()

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US'
)

def take_response(rawdata):
    audio = types.RecognitionAudio(content=rawdata)
    response = client.recognize(config, audio)
    return response.results

def text_to_speech(text):
    synthesis_input = texttospeech.types.SynthesisInput(text=text)
    voice = texttospeech.types.VoiceSelectionParams(language_code='en-US',ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = t2s.synthesize_speech(synthesis_input, voice, audio_config)
    return response.audio_content
