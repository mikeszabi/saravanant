import nautilus
import imdb
import gtk
import re
import os
import logging

MOVIE_MIMES = ['.wmv', '.mpg', '.mpeg', '.flv', '.mov', '.avi']

class IMDBPropertyPageExtension(nautilus.PropertyPageProvider):
    def __init__(self):
        logging.basicConfig(filename='/tmp/sara-nautilus-debug',level=logging.ERROR)

    def getAttrFromArray(self,elemArray,nameOfAttr):
        result = ",".join( [el[nameOfAttr] for el in elemArray])
        return result

    def getMovieAttributes(self):
        #Ignoring plot and mpaa as it screws up alignment
        movieDtlsArr = ["Title","Movie Id","Rating","Votes","Director(s)","Writer(s)","Released In","Genre(s)", "Runtime", "Cast", "Original Music"]
        return movieDtlsArr

    def getIMDBDtls(self,movieName):
        ia = imdb.IMDb()
        sResult = ia.search_movie(movieName)
        movieDtlsArr = self.getMovieAttributes()
        movieDtlsHash = {}
        for elemName in movieDtlsArr:
            movieDtlsHash[elemName] = ""

        if len(sResult) > 0 :
            topResult = sResult[0]
            ia.update(topResult)

            movieDtlsHash["Title"] = topResult['title']
            movieDtlsHash["Movie Id"] = topResult.movieID
            movieDtlsHash["Rating"] = str(topResult['rating'])
            movieDtlsHash["Votes"] = str(topResult['votes'])
            movieDtlsHash["Director(s)"] = self.getAttrFromArray(topResult['director'], 'name')
            movieDtlsHash["Writer(s)"] = self.getAttrFromArray(topResult['writer'], 'name')
            movieDtlsHash["Released In"] = str(topResult['year'])
            movieDtlsHash["Genre(s)"] = ",".join(topResult['genre'])
            #movieDtlsHash["Plot"] = topResult['plot outline']
            #movieDtlsHash["MPAA"] = topResult['mpaa']
            movieDtlsHash["Runtime"] = str(topResult['runtimes'][0]) + " minutes"
            movieDtlsHash["Cast"] = self.getAttrFromArray(topResult['cast'][0:4], 'name')
            movieDtlsHash["Original Music"] = self.getAttrFromArray(topResult['original music'], 'name')
        return movieDtlsHash

    def getHBoxForAttr(self,attrName, movieDtlsHash):
        hbox = gtk.HBox(0, False)
        hbox.show()

        label = gtk.Label(attrName)
        label.show()
        hbox.pack_start(label)

        value_label = gtk.Label()
        value_label.set_text(movieDtlsHash[attrName])
        value_label.show()
        hbox.pack_start(value_label)
        return hbox
    
    def get_property_pages(self,files):
        if len(files) != 1:
            return
        
        fileObj = files[0]
        if fileObj.get_uri_scheme() != 'file':
            return

        if fileObj.is_directory():
            return

        fileName = fileObj.get_name() 
        #Stripping extension
        [fileName, extension]= os.path.splitext(fileName)
        if extension not in MOVIE_MIMES:
            return 

        #replace _ and - to spac for better results
        pattern = re.compile("eng|dvdrip|-|_|\[|\]|\.|axxo|fxg|xvid|r5", re.IGNORECASE)
        fileName = pattern.sub(" " , fileName)
        
        movieDtlsHash = self.getIMDBDtls(fileName)

        self.property_label = gtk.Label('IMDB Details')
        self.property_label.show()

        self.hbox = gtk.HBox(0, False)
        self.hbox.show()

        self.vbox = gtk.VBox(0,False)
        self.vbox.show()

        for attributes in self.getMovieAttributes():
            self.vbox.pack_start(self.getHBoxForAttr(attributes, movieDtlsHash))

        self.hbox.pack_start(self.vbox)
        
        return nautilus.PropertyPage("NautilusPython::imdb_dtls", self.property_label, self.hbox),
