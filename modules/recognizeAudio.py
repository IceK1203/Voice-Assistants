import speech_recognition as sr

def recognize_audio(wakeword):
    a = sr.Recognizer()

    done = False
    while not done:
        try:
            print("Say something...")
            with sr.Microphone() as mic:
                a.adjust_for_ambient_noise(mic, duration=0.2)
                audio = a.listen(mic, phrase_time_limit=1)
                user = a.recognize_google(audio)
                #print("You said: " + user)


                if wakeword in user.lower():
                    print("Now taking a command...")
                    a.adjust_for_ambient_noise(mic, duration=0.2)
                    NewAudio = a.listen(mic, phrase_time_limit=2)
                    userCommand = a.recognize_google(NewAudio)
                        
                    #print("The AI Thinks you said: " + userCommand)
                    done = True

        except sr.UnknownValueError:
            # if the voice is unclear
            print("Could not understand")
            continue

        except sr.RequestError as e:
            print("Error; {0}".format(e))
            continue

    return userCommand