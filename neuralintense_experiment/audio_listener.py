import pyaudio


class AudioListener:
    def __init__(
        self,
        input_format: int = pyaudio.paInt16,
        channels: int = 2,
        rate: int = 441000,
        is_input: bool = True,
        chunk: int = 1024
    ):
        self.p = pyaudio.PyAudio()
        self.input_format = input_format
        self.channels = channels
        self.rate = rate
        self.is_input = is_input
        self.chunk = chunk

    def __enter__(self):
        print("Try to open audio stream...")
        self.audio_stream = self.p.open(
            format=self.input_format,
            channels=self.channels,
            rate=self.rate,
            input=self.is_input,
            output=self.is_input
        )
        print("Audio stream opened successfully!")
        return self.audio_stream

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit audio stream...")
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.p.terminate()
        print("Audio stream closed successfully!")
