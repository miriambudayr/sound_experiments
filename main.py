import pydub
from pydub.playback import play

song = pydub.AudioSegment.from_wav("bbc_comedy_machines.wav")

print('this is the song', song)
play(song)
