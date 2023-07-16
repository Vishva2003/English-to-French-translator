from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText= MyMemoryTranslator(source="english",target="french").translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText= MyMemoryTranslator(source="french",target="english").translate(frenchText)
    return englishText