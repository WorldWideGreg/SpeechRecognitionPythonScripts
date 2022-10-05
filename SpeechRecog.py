import speech_recognition as sr
import threading

# Parse the sentence to find words searched then if so use set_data


def parse_sentence(sentence):
    print(sentence)


def main():
    try:
        print("Programme lancé. Microphone actuellement utilisé :")
        print(sr.Microphone(device_index=1))
        while(True):
            r = sr.Recognizer()
            with sr.Microphone(device_index=0) as source:
                audio = r.listen(source)
            try:
                sentence = r.recognize_google(audio, language="fr-FR")
                t = threading.Thread(target=parse_sentence, args=(sentence,))
                t.start()
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Le service Google Speech API ne fonctionne plus\n {}" + format(e))
    except KeyboardInterrupt:
        print("Fin du programme.")
        exit()


if __name__ == "__main__":
    main()
