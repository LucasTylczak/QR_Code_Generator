import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

# Initialiser le traducteur
translator = Translator()

# Fonction pour la reconnaissance vocale et la traduction
def speech_to_text_and_translate(source_lang='auto', target_lang='en'):
    # Configuration du recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = recognizer.listen(source)

        try:
            # Reconnaissance vocale
            text = recognizer.recognize_google(audio, language=source_lang)
            print("Vous avez dit:", text)

            # Traduction
            translation = translator.translate(text, src=source_lang, dest=target_lang)
            translated_text = translation.text
            print("Traduction:", translated_text)

            # Synthèse vocale de la traduction
            engine.say(translated_text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Impossible de comprendre l'audio.")
        except sr.RequestError as e:
            print("Erreur lors de la demande de service de reconnaissance vocale : {0}".format(e))
        except Exception as e:
            print("Une erreur s'est produite : ", str(e))

# Tester la fonction
while True:
    speech_to_text_and_translate()
