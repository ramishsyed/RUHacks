def translator (descriptions,lang):
    from googletrans import Translator
    translator = Translator()
    translated = translator.translate(descriptions, src='en', dest=lang)
    return translated.text
