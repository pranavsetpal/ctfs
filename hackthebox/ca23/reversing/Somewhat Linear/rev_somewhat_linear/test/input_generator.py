import numpy as np
import soundfile as sf

flag, rate = sf.read('./flag.wav')

# randomly shuffle the frequencies
freqs = np.fft.rfftfreq(len(flag), 1.0/rate)
filter_frequency_response = np.random.uniform(-10, 10, len(freqs))

# get the amplitudes
def filter(sample):
    amplitudes = np.fft.rfft(sample)
    shuffled_amplitudes = amplitudes * filter_frequency_response
    print(f"RFFT: {len(shuffled_amplitudes)}")
    print(f"VALS: {shuffled_amplitudes}")

    return np.fft.irfft(shuffled_amplitudes)

impulse = np.zeros(len(flag))
impulse[0] = 1

print(f"IMPL: {len(impulse)}")
shuffled_signal = filter(impulse)
print(f"SHUF: {len(shuffled_signal)}")
sf.write('impulse_response.wav', shuffled_signal, rate)

shuffled_flag = filter(flag)
sf.write('shuffled_flag.wav', shuffled_flag, rate)
