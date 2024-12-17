from audio_listener import AudioListener

import numpy as np
from openwakeword.model import Model

wwd_model = Model(
    vad_threshold=0.9
)

sample_rate =16000
channels = 1
frame_rate = 625

try:
    with AudioListener(
        rate=sample_rate,
        channels=channels,
        chunk=frame_rate,
    ) as audio_stream:
        while True:
            pcm = audio_stream.read(frame_rate)
            pcm = np.frombuffer(pcm, dtype=np.int16)

            prediction = wwd_model.predict(pcm, timing=True)
            prediction = prediction[0]
            max_key = max(zip(prediction.values(), prediction.keys()))[1]
            print(max_key)
except Exception as e:
    print(e)
