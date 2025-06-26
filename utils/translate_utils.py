from googletrans import Translator

def translate_text(text, dest_lang="hi"):
    return Translator().translate(text, dest=dest_lang).text
