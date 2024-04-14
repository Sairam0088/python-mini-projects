# voice recorder using python

import sounddevice as sd
from scipy.io.wavfile import write
freq = 44100 #44100 - 48000 usally
duration = 5
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()

write("recording.mp3", freq, recording)

