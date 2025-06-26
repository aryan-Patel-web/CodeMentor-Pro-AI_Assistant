from gtts import gTTS

def generate_tts(text, output_file="summary.mp3", lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    return output_file
