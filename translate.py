from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, dest="en")
    return translated.text

if __name__ == '__main__':
    text = "素晴らしい発表でした!"

    a = translate_text(text)
    print(a)
