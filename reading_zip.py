#Reading contents of ZIP file
import zipfile

#make sure to keep the python file and .zip file in same directory or provide the absolute path.
MyFolderZip = zipfile.ZipFile('MyFolder.zip')
f = MyFolderZip.namelist()
print(f)
