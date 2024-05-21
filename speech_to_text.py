#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the streaming API.

NOTE: This module requires the additional dependency `pyaudio`. To install
using pip:

    pip install pyaudio

Example usage:
    python transcribe_streaming_mic.py
"""

# [START speech_transcribe_streaming_mic]
from __future__ import division

import re
import sys
import time

from multiprocessing import Process

from google.oauth2 import service_account
from google.cloud import speech
import google

import pyaudio
from six.moves import queue

###############################
from ctypes import *

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    return


c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)
# Initialize PyAudio
###############################

# Audio recording parameters
RATE = 44100 # 기존 16000 에서 "OSError: [Errno -9997] Invalid sample rate" 발생
CHUNK = int(RATE / 10)  # 100ms


import time

from openpibo.device import Device
d = Device()

touch_count = 0     # 밖으로 빼야 함수 부를 때마다 초기화 안 됨

def touch():
    """
    터치 2번으로 발생시켜서 stt 탈출하는 기능

    Raises:
        Exception: stt 탈출!
    """
    # print("tt")
    # timelimit = time.time() + timeout    
    global touch_count
    
    # while time.time() < timelimit:
    #     data = d.send_cmd(d.code_list['SYSTEM']).split(':')[1].split('-')
    #     result = data[1] if data[1] else "No signal"
        
    #     if result == "touch":
    #         touch_count += 1
    #         print("touch:", touch_count)
            
    #         if touch_count % 2 == 0:
    #             d.eye_on(255,245,80)
    #             raise Exception("탈출") 
        
    #     else:
    #         continue
    data = d.send_cmd(d.code_list['SYSTEM']).split(':')[1].split('-')
    result = data[1] if data[1] else "No signal"
    
    if result == "touch":
        touch_count += 1
        print("touch:", touch_count)
        
        if touch_count % 2 == 0:
            d.eye_on(255,245,80)
            raise Exception("탈출") 

    return touch_count



class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

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


def listen_print_loop(responses):
    global touch_count
    text = ''
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue       

        result = response.results[0]
                
        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))
        
        
        
        if not result.is_final:
            # sys.stdout.write(transcript + overwrite_chars + '\r')
            # sys.stdout.flush()
            try:
                touch()     # 뭔가 말 하면서 터치해야 함
                print('답변: ' + transcript + overwrite_chars, end='\r')
                num_chars_printed = len(transcript)
                                
            except Exception as e:
                text = "next"
                touch_count = 2
                break

        else:
            text = transcript + overwrite_chars
            break
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('Exiting..')
                break
            num_chars_printed = 0    
            
    return text, touch_count


def speech_to_text(timeout=10):
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = 'ko-KR'  # a BCP-47 language tag
    
    service_account.Credentials.from_service_account_file("/home/pi/stt-test-000-0226dec785df.json")
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        single_utterance = True,    # 공백 생기면 바로 입력 중단시킴!
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        print("\n답변: ", end='\r')
        requests = (speech.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests, timeout=timeout)
        
        # Now, put the transcription responses to use.
        stt_out = listen_print_loop(responses)
        print('답변:', stt_out[0])
    
        # print('\n')
    return stt_out

if __name__ == '__main__':
    speech_to_text()
        
# [END speech_transcribe_streaming_mic]
