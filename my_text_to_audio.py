from gtts import gTTS
from playsound import playsound

def play_audio(hello):
    playsound(hello)

def text_to_audio(text):
    my_audio=gTTS(text)
    my_audio.save("hello.mp3")
    play_audio("hello.mp3")

if __name__ == '__main__':
    name=input("Enter Your name: ")
    text_to_audio(f"hello {name} sir  how are you??")
