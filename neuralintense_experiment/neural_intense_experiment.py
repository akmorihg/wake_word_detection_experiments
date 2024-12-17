# import speech_recognition as sr
#
#
# recognizer = sr.Recognizer()
#
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = recognizer.listen(source)
#     print("Done!")
#
#     try:
#         recognized_text = recognizer.recognize_vosk(audio, language="ru-RU")
#         print(recognized_text)
#     except Exception as ex:
#         print(ex)

import nltk
nltk.download('punkt_tab')

from neuralintents.assistants import BasicAssistant

assistant = BasicAssistant("intents.json")
assistant.fit_model(epochs=10)

assistant.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        print(assistant.process_input(message))
