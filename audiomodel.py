import edge_tts
import asyncio
import pygame
import json
# ---------------------------
# AUDIO (JSON + TTS)
# ---------------------------
class AuidoModel:
    def __init__(self, file_path):
        self.file_path = file_path

    def open_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def search_text(self, class_id):
        self.text = self.data["texts"][class_id]["text"]

    def text_to_speech(self):
        async def generate():
            tts = edge_tts.Communicate(self.text, "ar-EG-ShakirNeural")
            await tts.save("voice.mp3")

        asyncio.run(generate())
        pygame.mixer.init()
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass


