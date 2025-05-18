import wave
import numpy as np
from scipy.io.wavfile import write

audio = wave.open(r"C:\Users\DELL\Downloads\Beethoven_Diabelli_Variation_No._13.wav", 'rb')
secret = "good job my child, you have conquered all the obstacles i have bestowed upon you"

# ----------------------------------------------------------------------------------------------------------------------

n_channels = audio.getnchannels()
sample_width = audio.getsampwidth()
frame_rate = audio.getframerate()
n_frames = audio.getnframes()

# ----------------------------------------------------------------------------------------------------------------------

secret_bits = ''.join(f"{ord(s):08b}" for s in secret)
secret_bits += '00000000'

# ----------------------------------------------------------------------------------------------------------------------

audio_raw_frames = audio.readframes(audio.getnframes())
audio_int_vals = np.frombuffer(audio_raw_frames, dtype=np.int16)


if n_channels == 2:
    left_channel = audio_int_vals[::2].copy()
    right_channel = audio_int_vals[1::2].copy()
    target_channel = left_channel
else:
    target_channel = audio_int_vals.copy()


audio_binaries = np.array([f"{int(i) & 0xFFFF:016b}" for i in target_channel])
audio_binaries = np.array([[int(bit) for bit in dbyte] for dbyte in audio_binaries], dtype=np.uint8)

# ----------------------------------------------------------------------------------------------------------------------

sb_index = 0
encoded_channel = []

for audio_sample in audio_binaries:
    if sb_index < len(secret_bits):
        audio_sample[-1] = np.uint8(secret_bits[sb_index])
        sb_index += 1

    replaced_audio_sample = ''.join(str(bit) for bit in audio_sample)
    replaced_audio_sample = int(replaced_audio_sample, 2)
    if replaced_audio_sample > 32767:
        replaced_audio_sample -= 65536
    encoded_channel.append(np.int16(replaced_audio_sample))

# ----------------------------------------------------------------------------------------------------------------------

encoded_channel.extend(target_channel[len(encoded_channel):])
encoded_channel = np.array(encoded_channel, dtype=np.int16)

# ----------------------------------------------------------------------------------------------------------------------

# Reconstruct full audio if stereo
if n_channels == 2:
    new_audio = np.empty((encoded_channel.size + right_channel.size,), dtype=np.int16)
    new_audio[::2] = encoded_channel
    new_audio[1::2] = right_channel
else:
    new_audio = encoded_channel


write(r"C:\Users\DELL\Downloads\hi\encoded.wav", 44100, new_audio.reshape(-1, 2))
