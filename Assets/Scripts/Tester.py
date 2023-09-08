import nltk
from nltk.corpus import stopwords
import string
import BaseDictionary as bd
nltk.download('stopwords')

# Setting the spanish stopwords
stemmer = nltk.SnowballStemmer("spanish")
stopword=set(stopwords.words('spanish'))

string1 = "Los libros están en el estante."
string2 = "Las llaves del coche están en el bolsillo."
string3 = "El perro duerme en la cama."
string4 = "La cartera está en el bolso."
string5 = "La tarea está en la mochila."
string6 = "Los zapatos están en el armario."
string7 = "La bicicleta está en el garaje."
string8 = "El teléfono está en la mesa de la cocina."
string9 = "Los documentos están en el cajón."
string10 = "La pelota está en el jardín."


bd.addTask([word for word in string1.lower().split(' ') if word not in stopword], string1)
bd.addTask([word for word in string2.lower().split(' ') if word not in stopword], string2)
bd.addTask([word for word in string3.lower().split(' ') if word not in stopword], string3)
bd.addTask([word for word in string4.lower().split(' ') if word not in stopword], string4)

values = bd.checkAllTask()
for element in values:
	print(element)

print("-------------------")
print(bd.checkForItem([word for word in string1.lower().split(' ') if word not in stopword]))
print(bd.checkForItem([word for word in string3.lower().split(' ') if word not in stopword]))
print(bd.checkForItem([word for word in string8.lower().split(' ') if word not in stopword]))


