import speech_recognition as sr
import datetime
import pyttsx3
import os
import subprocess
import webbrowser
import openai 

openai.api_key= "Token-OpenAI"

engine = pyttsx3.init()

#Funcion para la operación abrir google
def abrir_chatgpt(pregunta):
    while True:
        prompt = input("\nIntroduce una pregunta: ")
        if prompt == "exit":
            break
    completion = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=2048)
    print(completion.choices[0].text)

#Función para reproducir una canción en la plataforma elejida
def abrir_cancion(cancion, plataforma):
    if plataforma == "spotify":
        os.startfile("spotify:" + cancion)
        
    elif plataforma == "youtube" or plataforma == 'Youtube':
        webbrowser.open("https://www.youtube.com/results?search_query=" + cancion)

#Funcion para la operación abrir google
def abrir_google(pregunta):
    webbrowser.open("https://www.google.com/search?q=" + pregunta)

#Funcion para la operación abrir calendario
def abrir_calendario():
    if os.name == "nt":
        os.startfile("outlookcal:")
    else:
        subprocess.Popen(["open", "-a", "Calendar"])

#Imprime un mesaje de bienvenida y espera el comando a mencionar
def asistente_virtual():
    print("Hola, ¿en qué puedo ayudarte hoy?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        pregunta = r.recognize_google(audio, language="es-ES")
        print("Dijiste: " + pregunta)

#Te imprime la hora actual y aparte de lo dice 
        if "hora" in pregunta:
            ahora = datetime.datetime.now()
            hora_actual = "La hora actual es " + str(ahora.hour) + ":" + str(ahora.minute)
            print(hora_actual)
            engine.say(hora_actual)
            engine.runAndWait()

#Te imprime la fecha actual y te la menciona
        elif "fecha" in pregunta:
            hoy = datetime.datetime.now()
            fecha_actual = "Hoy es " + hoy.strftime("%d/%m/%Y")
            print(fecha_actual)
            engine.say(fecha_actual)
            engine.runAndWait()

#Abre el calendario 
        elif "calendario" in pregunta:
            abrir_calendario()

#Abrir google y buscar lo que se mencione
        elif "google" in pregunta:
            print ("¿Que deseas buscar?: ")
            abrir_google(pregunta)

#Abrir chatGPT y buscar lo que se mencione
        elif "chat gpt" in pregunta:
            abrir_chatgpt(pregunta) 

#Abre spotify o youtube dependiendo cual se elija y reproduce la canción que se pida
        elif "reproducir" in pregunta:
            cancion = pregunta.split("reproducir")[-1].strip()
            plataforma = ""
            if "en spotify" in pregunta:
                plataforma = "spotify"
            elif "en youtube" in pregunta:
                plataforma = "youtube"
            if plataforma:
                abrir_cancion(cancion, plataforma)
            else:
                print("No especificaste en qué plataforma quieres reproducir la canción.")

#Mensaje que se arroja si no entendio la petición 
        else:
            engine.say("Lo siento, no entiendo lo que quieres decir. ¿Podrías reformular la pregunta?")
            engine.runAndWait()
    except:
        print("No pude escuchar lo que dijiste, ¿podrías repetirlo?") #Mensaje si no tiene sentido la petición 

asistente_virtual()