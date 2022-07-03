import speech_recognition as sr
print(sr.__version__) # just to print the version not required


def speech_input():
    try:
        r = sr.Recognizer()
        my_mic = sr.Microphone(device_index=2) #my device index is 1, you have to put your device index
        with my_mic as source:
            print("Say now!!!!")
            r.adjust_for_ambient_noise(source) #reduce noise
            audio = r.listen(source) #take voice input from the microphone
        return(r.recognize_google(audio)) #to print voice into text
    except:
        return("*mumble*")