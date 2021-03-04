#Creating ZIP files
import zipfile
MyFolder = zipfile.ZipFile('MyFolder.zip', 'w')   # to create Zipfile object must be opened in write mode, w
MyFolder.write('My Folder/fishing equipment.txt', compress_type = zipfile.ZIP_DEFLATED)
MyFolder.close()

#adding to ZIP files
import zipfile
MyFolder = zipfile.ZipFile('MyFolder.zip', 'a')  #to add to existing file the second arguement is append, a
MyFolder.write('My Folder/stern trawler.txt', compress_type = zipfile.ZIP_DEFLATED)
MyFolder.close()

#adding to ZIP files
import zipfile
MyFolder = zipfile.ZipFile('MyFolder.zip', 'a')
MyFolder.write('My Folder/test.jpg', compress_type = zipfile.ZIP_DEFLATED)
MyFolder.close()