import urllib
from datetime import datetime, date, timedelta
import urlparse
import csv

#Assumes script runs on early hours of a day to gather stats of yesterday

#Using days=2. This is because Wordpress seems to use UTC time and some times yesterday is not returned.
data = urllib.urlopen('http://stats.wordpress.com/csv.php?api_key=apiKeyOfYourBlog&blog_id=blogId&table=referrers&days=2&limit=-1').read()
fileObj = open("filePath/blogReferrers.csv", "a")
csvWriterObj = csv.writer(fileObj);

dataArr = data.split("\n")
yesterday = datetime.now() - timedelta(days=1)
yesterdayStr = yesterday.strftime('%Y-%m-%d')

#Format date,referrer,views
for line in dataArr:
	try :
		lineDataArr = line.split(",")
		if lineDataArr[0] == yesterdayStr :
			parsedUrlResult = urlparse.urlparse(lineDataArr[1])
			lineDataArr.append(parsedUrlResult.netloc)
			csvWriterObj.writerow(lineDataArr)
	except ValueError:
		csvWriterObj.writerow(["Error : Cannot write Rown " +  line] );
fileObj.close()
