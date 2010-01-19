import urllib
import codecs
import simplejson
import sys 

#Input file might be potentially in other languages
def getAllWords(filename):
	f = codecs.open(filename,'r','utf-8')
	allWords = f.readlines();
	f.close()
	return allWords

def translateAString(word,src ='en',dest ='hi'):
	googleTranslateUrl = "http://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q=%(message)s&langpair=%(from)s%%7C%(to)s"
	actualUrl = googleTranslateUrl % { 'message': word, 'from': src,'to': dest}
	#Encode the url into utf-8 as url's cant contain strange characters
	actualUrl = actualUrl.encode('utf-8')
	data = urllib.urlopen(actualUrl).read()
	jsonData = simplejson.loads(data)
	if jsonData['responseStatus'] != 200:
		return 'error'
	return jsonData['responseData']['translatedText']

def writeToFile(fileHandle,word,translatedWord):
	fileHandle.write(word+'|'+translatedWord+'\n')

def translateFile(filename,src='en',dest='hi'):
	allWords = getAllWords(filename)
	f = codecs.open('translated_' + filename,'w','utf-8')
	for word in allWords:
		word = word.strip()
		writeToFile(f,word,translateAString(word,src,dest))
	f.close()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage : python translate.py [srclang] [destlang]\n"
		exit(-1)
	if len(sys.argv) == 2:
		translateFile(sys.argv[1])
	if len(sys.argv) == 3:
		translateFile(sys.argv[1],sys.argv[2])
	if len(sys.argv) >= 4:
		translateFile(sys.argv[1],sys.argv[2],sys.argv[3])
