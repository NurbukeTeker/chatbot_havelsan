from __future__ import division

import re
import sys

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


def get_current_time():
    """Return Current Time in MS."""

    return int(round(time.time() * 1000))


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        # self.start_time = get_current_time()
        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

import time 
def listen_print_loop(responses):
    
    # print(responses)
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        # print(response)
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:  
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))

        if not result.is_final:     
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:          
            # print('_____________________________')
            print(transcript + overwrite_chars) # == print(transcript)

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                # print('Exiting..')
                break

            num_chars_printed = 0
            return transcript


def speechToText():
    print("Listening")
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = 'tr-TR'  # a BCP-47 language tag

#    client = speech.SpeechClient.from_service_account_json("D:\SpyderProjects\BitBucket\oyak-poc\jsonFiles\speechtotext.json")
    client = speech.SpeechClient.from_service_account_json("jsonFiles\\speechtotext.json")
    print("FileFound")
    # client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        
        audio_generator = stream.generator()
        
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)
        
        start = time.time()
        # Now, put the transcription responses to use.
        answer = listen_print_loop(responses)
        print('5 *********' + answer)
    print("Final Answer " + answer)
    return answer
        

def textToSpeech(text, speed=1.1):
    print('speed: ', speed)
    import html
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient.from_service_account_json("jsonFiles\\texttospeech.json")
   
    escaped_lines = html.escape(text)

    # Convert plaintext to SSML
    # Wait two seconds between each address
#    ssml = '<speak>{}</speak>'.format(text)
#    ssml = '<speak>{}</speak>'.format(escaped_lines.replace('\n', '<break time="500ms"/>').replace('. ', '<break time="250ms"/>').replace(', ', '<break time="200ms"/>'))

    ssml = '<p><s>{}</s></p>'.format(escaped_lines.replace('\n', '</s><s>').replace('. ', '</s><s>').replace(', ', '<break time="200ms"/>').replace('-', '<break time="200ms"/>').replace('&ensp;','').replace('<br>',' '))

    # Sets the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml)

    # Builds the voice request, selects the language code ("en-US") and
    # the SSML voice gender ("MALE")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='tr-TR',
        name = 'tr-TR-Standard-D', #https://cloud.google.com/text-to-speech/docs/voices --> istediğimiz ses tonu
        ssml_gender = texttospeech.enums.SsmlVoiceGender.FEMALE)
    
#    voice = texttospeech.types.Voice(
#            natural_sample_rate_hertz=4,
#            language_codes='tr-TR',
#            name = 'tr-TR-Standard-C', #https://cloud.google.com/text-to-speech/docs/voices --> istediğimiz ses tonu
#            ssml_gender = texttospeech.enums.SsmlVoiceGender.FEMALE)

    # Selects the type of audio file to return
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
        speaking_rate = speed, #speed: [0.25, 4.0]
        pitch = 2.0, #semitone: [-20.0, 20.0]
        sample_rate_hertz = 44100,
        volume_gain_db = 0.0 #volume: [-96.0, 16.0]
        ) 

    # Performs the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    
    from io import BytesIO
    import pygame
          
    bytesIO = BytesIO(response.audio_content)
              
    pygame.mixer.init()
    pygame.mixer.music.load(bytesIO)
    pygame.mixer.music.play()
    
#    # The response's audio_content is binary.
#    with open('output.mp3', 'wb') as out:
#        # Write the response to the output file.
#        out.write(response.audio_content)
#        print('Audio content written to file "output.mp3"')
        

#textToSpeech('hâla çalışıyorum')
    
    
    
def speechToTextFree():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = "tr-TR")
            print("You said : {}".format(text) )
            return text
        except Exception as e:
            print(e)
            return -1
        
        
    speechToTextFree()
        