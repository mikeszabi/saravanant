import urllib
from time import strftime,localtime
import os

data = urllib.urlopen('http://stats.wordpress.com/csv.php?api_key=apiKeyOfYourBlog&blog_id=blogId&days=2').read()

curTimeTuple = localtime()
curHr = curTimeTuple[3]

fileObj = open("filePath/blogDayStats.csv", "a")

dataArr = data.split()
try:
	if curHr == 0 :
		curDayStats = dataArr[1]
		curTimeStr = "23:59:00"
	else :
		curDayStats = dataArr[-1]
		curTimeStr = strftime("%H:00:00", curTimeTuple)
except ValueError:
	fileObj.write("Error : Got " + data );

try :
#	fileObj.write("");
	[curDay,curStats]  = curDayStats.split(",")
	dataToWrite = curDay + "," + curTimeStr + "," + curStats + "\n"
	fileObj.write(dataToWrite)
except ValueError:
	fileObj.write("Error2 : Got " + curDayStats + " and orig data was " + data);

fileObj.close()
