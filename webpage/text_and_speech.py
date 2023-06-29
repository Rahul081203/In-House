# from translate import Translator
import speech_recognition as sr
from gtts import gTTS
from langdetect import detect
# import playsound as ps
# import pygame
import os
from googletrans import Translator
import time


# def text_to_text(input_string, destination):
#     source_lang = detect(input_string)
#     translator = Translator(from_lang=source_lang, to_lang=destination)
#     translated = translator.translate(input_string)
#     return translated
def text_to_text(input_string,destination):
  translator = Translator()
  translated = translator.translate(input_string,dest=destination)
  return translated.text

def text_to_text_source(input_string,source,destination):
    translator = Translator()
    translated = translator.translate(dest=destination,src=source,text=input_string)
    return translated.text
# def speech_to_text():
#     recognizer = sr.Recognizer()
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 recognizer.adjust_for_ambient_noise(source, duration=0.2)
#                 audio = recognizer.listen(source)
#                 text = recognizer.recognize_google(audio)
#                 text = text.lower()
#                 return text
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
#             break
#         except sr.UnknownValueError:
#             print("Could not understand")
#             break

# def speech_to_text():
#     Recognizer = sr.Recognizer()
#     while (True):

#         # Runtime exception handling
#         try:
#             # microphone as source
#             with sr.Microphone() as source:
#                 # Adjusting the user input to eliminate noise above threshold
#                 Recognizer.adjust_for_ambient_noise(source, duration=0.2)

#                 # listens for the user's input
#                 audio = Recognizer.listen(source)

#                 # Using google to recognize audio
#                 text = Recognizer.recognize_google(audio)
#                 text = text.lower()

#                 return text

#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
#             break;

#         except sr.UnknownValueError:
#             print("Could not understand")
#             break;

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return "Speech not understood";
    except sr.RequestError as e:
        print(f"Error occurred during speech recognition: {str(e)}")
    
    return ""   

# def remove_translated_file():
#     if os.path.exists('translated.mp3'):
#         time.sleep(1)  # Add a delay of 1 second
#         os.remove('translated.mp3')

# def text_to_speech(input_string, lang):
#     voice = gTTS(text=input_string, lang=lang)
#     voice.save('translated.mp3')

#     pygame.init()  # Initialize pygame

#     pygame.mixer.init()
#     pygame.mixer.music.load("translated.mp3")

#     # Set an event to trigger when the music finishes playing
#     pygame.mixer.music.set_endevent(pygame.USEREVENT)

#     pygame.mixer.music.play()

#     # Wait for the music to finish playing
#     pygame.event.wait()

#     pygame.mixer.music.stop()

#     # Remove the 'translated.mp3' file
#     remove_translated_file()

def remove_translated_file():
    file_path = r'c:\users\rahul\documents\ntcc_4th_sem\webpage\static\translated.mp3'
    if os.path.exists(file_path):
        os.remove(file_path)
def text_to_speech(input_string, lang):
    voice = gTTS(text=input_string, lang=lang)
    voice.save(r'c:\users\rahul\documents\ntcc_4th_sem\webpage\static\translated.mp3')
    



# def input_as_text():
#     input_string = input('Enter text: ')
#     destination = input('Enter destination language code: ')
#     output = text_to_text(input_string, destination)
#     print(output)
#
#     correct = input("Is the translation correct? (Y/n)")
#     if correct in ['n', 'N']:
#         source_lang = input("Try entering the source language manually\nLanguage : ")
#         output = text_to_text_source(input_string, source_lang, destination)
#         print("Translated: " + output)
#     choice = input('Would you like to hear the pronunciation? (Y/n): ')
#     if choice.lower() == 'y':
#         text_to_speech(output, destination)
#         # os.remove('translated.mp3')
# def input_as_speech():
#     destination = input("Enter the destination language: ")
#     text = speech_to_text()
#     output = text_to_text(text, destination)
#     print('Translated: ' + output)
#     text_to_speech(output, destination)
#     correct = input("Is the translation correct? (Y/n)")
#     if correct in ['n', 'N']:
#         source_lang = input("Try entering the source language manually\nLanguage : ")
#         output = text_to_text_source(text,source_lang,destination)
#         print("Translated: "+output)
#         text_to_speech(output,destination)
#         # os.remove('translated.mp3')
# def translator():
#     print("######## =========  MENU  ========= ########")
#     print("1                    :         Input as Text")
#     print("2                    :         Input Speech")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         input_as_text()
#     elif choice == 2:
#         input_as_speech()
#     else:
#         print("Invalid choice.")
#
# translator()
