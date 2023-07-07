import numpy as np
from scipy.fft import *
import soundfile as sf

shuffle_flg, shuffle_flg_rate = sf.read('./shuffled_flag.wav')

impulse_res, impulse_res_rate = sf.read('./impulse_response.wav')
impulse = np.zeros(len(impulse_res))
impulse[0] = 1

impulse_amplitudes = np.fft.rfft(impulse)
impulse_res_amplitudes = np.fft.rfft(impulse_res)

filter_frequency_response = np.real(impulse_res_amplitudes / impulse_amplitudes)

flag = np.fft.irfft(np.fft.rfft(shuffle_flg) / filter_frequency_response)

sf.write("./flag.wav", flag, shuffle_flg_rate)
