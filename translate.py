def translator (descriptions):
    from googletrans import Translator
    translator = Translator()
    translated = translator.translate(descriptions, src='en', dest='fr')
    return translated.text
