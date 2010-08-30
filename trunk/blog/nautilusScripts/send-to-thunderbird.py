import nautilus
import urllib
import subprocess
import logging

class SendToThunderbirdExtension(nautilus.MenuProvider):
    def __init__(self):
        logging.basicConfig(filename='/tmp/sara-nautilus-debug',level=logging.DEBUG)
    
    def menu_activate_cb(self, menu, files):
        allAttachments = ""
        for fileObj in files:
            #Check if file still exists
            if fileObj.is_gone():
                return
            #To handle files with special characters !
            filename = urllib.unquote(fileObj.get_uri())
            allAttachments = allAttachments + filename + ","

        #Strip last ,
        allAttachments = allAttachments[:-1]
        callString = "/usr/bin/thunderbird -compose \"attachment='" + allAttachments + "'\""
        #logging.debug(blah)
        subprocess.call(["/usr/bin/thunderbird", "-compose", "attachment='" + allAttachments + "'"])
        
    def get_file_items(self, window, files):
        if len(files) == 0:
            return

        #For only (local) files
        for fileObj in files:
            if fileObj.get_uri_scheme() != 'file':
                return
            if fileObj.is_directory() :
                return
        item = nautilus.MenuItem('Nautilus::send_to_thunderbird',
                                 'Send selected files to Thunderbird as attachment',
                                 'Send selected files to Thunderbird as attachment')
        item.connect('activate', self.menu_activate_cb, files)
        return item,

    if __name__ == '__main__':
        #Theoretically not needed as import nautilus will fail !
        import sys
        print 'This is a nautilus extension and cannot be invoked - Install nautilus-python and put them under ~/.nautilus/python-extensions with executable permissions set !'
        sys.exit(1)
        

