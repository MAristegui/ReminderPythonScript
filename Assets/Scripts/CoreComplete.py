import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import string
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
nltk.download('stopwords')

# Setting the spanish stopwords
stemmer = nltk.SnowballStemmer("spanish")
stopword=set(stopwords.words('spanish'))

# Setting the speak and audio recognizer engines
engine = pyttsx3.init()
engine.setProperty('rate',125)
listener = sr.Recognizer()

# Activation phrase
target_phrase = "activar sistema"
# Checking phrase
check_phrase = "consultar valores"

dict = {}
while True:
	with sr.Microphone() as micro:
		print("Diga algo: ")
		sonido = listener.listen(micro)

		try:
			texto = listener.recognize_google(sonido, language="ES")
			print("Texto inicial: "+texto)
			#texto = [word for word in texto.split(' ') if word not in stopword]
			#print(texto)

			if target_phrase in texto:
				print("Se detecto la frase de activacion.")
				engine.say("Enetendido. Dime que necesitas")
				engine.runAndWait()
				while True:
					with sr.Microphone() as micro2:
						sonido = listener.listen(micro2)
						textoAGuardar = listener.recognize_google(sonido, language="ES")
						print(textoAGuardar)
						engine.say(textoAGuardar)
						engine.runAndWait()
						engine.say("Eso es correcto?")
						engine.runAndWait()
						sonido = listener.listen(micro2)
						texto = listener.recognize_google(sonido, language="ES")
						print("Texto encontrado:" +texto)

						if "sí" in texto:
							engine.say("entendido")
							engine.runAndWait()
							textClean = [word for word in textoAGuardar.split(' ') if word not in stopword]
							dict.update({textClean[0]:textoAGuardar})
							for clave, valor in dict.items():
								print(f"Clave: {clave}, Valor: {valor}")
							break
						elif "no" in texto:
							engine.say("Perdon, repita de nuevo en unos momentos")
							engine.runAndWait()
						else:
							engine.say("Lo lamento, no detecte ninguna respuesta")
							engine.runAndWait()

			if check_phrase in texto:
				engine.say("Entendido. Estas son las entradas que tengo almacenadas")
				engine.runAndWait()
				for clave, valor in dict.items():
					engine.say(valor)
					engine.runAndWait()

		except sr.UnknownValueError:
			print("No se pudo entender el audio")
		except sr.RequestError as e:
			print("Error en la solicitud a Google API; {0}".format(e))