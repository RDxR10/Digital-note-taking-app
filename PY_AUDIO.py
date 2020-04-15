import speech_recognition as sr
r=sr.recognizer
while True:
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("Say something")
    audio=r.listen(source)
    print(Done!)
    try:
      text = r.recognize_google(audio, language = 'en-US')
      print(text)
      print(r.recognize_google(audio))
    except:
      print("something meant wrong");
