dict = {}

#	wordArray: array of non-stop words
#	stringTask: Phrase to save
def addTask(wordArray, stringTask):
	dict.update({wordArray[0]:stringTask})

#	wordArray: array of non-stop words
def removeTask(wordArray):
	dict.pop(wordArray[0],None) # None avoid errors when the key doens't exist

def checkAllTask():
	return dict.values()

#	if key doesn't exist, return none
def checkForItem(wordArray):
	print(":::"+wordArray[0]
	return dict.get(wordArray[0],None)

