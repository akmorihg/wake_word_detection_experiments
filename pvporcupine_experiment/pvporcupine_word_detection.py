import struct

import pvporcupine

from audio_listener import AudioListener


porcupine = None

try:
    porcupine = pvporcupine.create(
        access_key="3o4NPb25B55EdWcGGu0D4NSSEfDtsgjndLUkRrWanNsONQVKOhHpEw==",
        model_path="models/porcupine_alisa_model/porcupine_params_ru.pv",
        keyword_paths=["models/porcupine_alisa_model/porcupine_ru_keywords.ppn"],
    )

    with AudioListener(
        rate=porcupine.sample_rate,
        channels=1,
        chunk=porcupine.frame_length,
    ) as audio_stream:
        print(porcupine.sample_rate)
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Hotword Detected")
except Exception as e:
    print(e)
