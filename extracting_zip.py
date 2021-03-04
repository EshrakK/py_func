#Extracting all files from ZIP file
import zipfile

#make sure to keep the python file and .zip file in same directory or provide the absolute path.
MyFolder = zipfile.ZipFile('MyFolder.zip')

#provide the path of the directory for extracted folder
MyFolder.extractall('C:/Users/Eshrak/Programming/GitHub Repo/py_func/')
MyFolder.close()
