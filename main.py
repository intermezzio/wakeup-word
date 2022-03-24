from pocketsphinx import LiveSpeech
import pyaudio
from tkinter import *

class AudioMonitor:
    def __init__(self):
        self.keyword = "hello"
        self.transcript = ""

        self.refresh_tk()

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            input=True,
            frames_per_buffer=1024
        )

    def refresh_tk(self):
        try:
            self.root.destroy()
        except:
            pass

        self.root = Tk()
        self.root.title("Audio Monitor Tool")

        self.text_box = Text(
            self.root,
            height=12,
            width=40
        )

        self.text_box.pack(expand=True)
        self.text_box.config(bg="#ff7777")

    def run(self):
        speech = LiveSpeech(audio_file=self.stream)
        for phrase in speech:
            print(phrase)
            this_line = str(phrase)
            try:
                self.text_box.insert('end', this_line + " ")
            except:
                self.refresh_tk()
                self.text_box.insert('end', this_line + " ")

            self.transcript += this_line
            if self.keyword == this_line:
                self.root.mainloop()

if __name__ == "__main__":
    am = AudioMonitor()
    am.run()