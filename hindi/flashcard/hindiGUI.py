"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""

from PythonCard import model,dialog
import glob
import codecs
import random

class MyBackground(model.Background):
	dirName = "/home/neo/gLingua/python/hindi/translated/"
	direction = "Hindi2English"
	fileLen = 0 

	def populateDropDown(self):
		allFiles = glob.glob(self.dirName + "translated*txt")
		allFileNames = ["Chapter " + str(i) for i in range(1,len(allFiles)+1)]
		allFileNames.insert(0,"All")
		self.components.fileChoice.items = allFileNames
		self.fileLen = len(allFiles)

	def readAndParseFile(self,fileName):
		f = codecs.open(self.dirName + fileName)
		allLines = f.readlines()
		f.close()
		return allLines

	def loadFile(self,fileNumber):
		listOfWords = []
		if fileNumber != 0:
			fileName = "translated_chap" + str(fileNumber) + ".txt"
			listOfWords = self.readAndParseFile(fileName)
		else:
			for i in range(1,self.fileLen+1):
				fileName = "translated_chap" + str(i) + ".txt"
				listOfWords.extend(self.readAndParseFile(fileName))
		return listOfWords

	def showNextWordToGUI(self):
		if len(self.eligibleWords) == 0:
			dialog.messageDialog(self, 'All Words Are Exhausted','Alert !!')
			return
		self.selectedWord = random.choice(self.eligibleWords)
		self.eligibleWords.remove(self.selectedWord)
		self.selectedWordMeaning = self.languageMap[self.selectedWord]
		self.components.txtWord.text = self.selectedWord

	def parseListAndCreateMap(self,listOfWords):
		self.languageMap = {}
		self.eligibleWords = [] 

		for line in listOfWords:
			english,hindi = line.strip().split("|")
			if self.direction == "Hindi2English":
				self.languageMap[hindi] = english
				self.eligibleWords.append(hindi)
			else:
				self.languageMap[english] = hindi
				self.eligibleWords.append(english)
		self.showNextWordToGUI()

	def on_btnMeaning_mouseClick(self,event):
		self.components.txtMeaning.text = self.selectedWordMeaning
	
	def on_btnNextWord_mouseClick(self,event):
		self.components.txtMeaning.text = ''
		self.showNextWordToGUI()

	def on_btnLoadFile_mouseClick(self,event):
		self.components.txtWord.text = ''
		self.components.txtMeaning.text = ''

		self.direction = self.components.rgDirection.stringSelection
		chapterName = self.components.fileChoice.stringSelection
		fileNumber = self.components.fileChoice.items.index(chapterName)
		listOfWords = self.loadFile(fileNumber)
		self.parseListAndCreateMap(listOfWords)

	def on_initialize(self, event):
		self.populateDropDown()

if __name__ == '__main__':
	app = model.Application(MyBackground)
	app.MainLoop()
