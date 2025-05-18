# import numpy as np
# from scipy.io.wavfile import write
#
# rate = 44100
# data = np.random.uniform(-1, 1, rate) # 1 second worth of random samples between -1 and 1
# scaled = np.int16(data / np.max(np.abs(data)) * 32767)
# write('test.wav', rate//4, scaled)

import numpy as np
from PIL import Image
from scipy.io.wavfile import write

img = Image.open(r"C:\Users\DELL\Downloads\shinji.jpg").convert("L")
# img = img.transpose(Image.FLIP_TOP_BOTTOM)

width, height = img.size
image_pixels = np.array(img) / 255.0


sample_rate = 44100
min_freq = 300
max_freq = 10_000
slice_duration = 0.01


frequencies = np.linspace(min_freq, max_freq, height)
samples_per_slice = int(sample_rate * slice_duration)

# Waveform Generation --------------------------------------------

final_waveform = []

t = np.linspace(0, slice_duration, samples_per_slice, endpoint=False)

for col in range(width):
    slice_wave = np.zeros(samples_per_slice)
    for row in range(height):
        brightness = image_pixels[row, col]
        if brightness > 0.01:  # skip near-black for speed
            freq = frequencies[row]
            sine_wave = np.sin(2 * np.pi * freq * t) * brightness
            slice_wave += sine_wave

            print(sine_wave)
            exit()
            # print(sine_wave)
    final_waveform.append(slice_wave)

audio = np.concatenate(final_waveform)

# --- Normalize to 16-bit and write WAV file ---
audio /= np.max(np.abs(audio))  # Normalize to -1..1
audio_int16 = np.int16(audio * 32767)
write(r"C:\Users\DELL\Downloads\hi\output3.wav", sample_rate, audio_int16)