#!/usr/bin/python3

#importing all stuff
from os import listdir, system, path, getcwd



# directory to be checked

base_folder = "/home/technopy/Descargas/"


#directories to move stuff

images_folder = "/home/technopy/Imágenes/"
music_folder = "/home/technopy/Música/"
videos_folder = "/home/technopy/Videos/"
documents_folder = "/home/technopy/Documentos/"
books_folder = "/home/technopy/'Biblioteca de calibre'/"
programming_folder = "/home/technopy/Documentos/programming/"


#Defining extensions to check

Document_ext = [
    '.doc', '.docx' '.log', '.msg', '.odt', '.pages', 
    '.rtf', '.tex', '.txt', '.wpd', '.wps', '.tar', '.obj'
    '.csv', '.dat', '.ppt', '.pptx', '.pps', '.xml', '.xls',
    '.xlr', '.xlsx', '.rom', '.nes','.ttf', '.otf',
    '.7z', '.gz', '.rar', '.zip', '.iso', '.bin',
    '.bak', '.tmp', '.torrent', '.msi']

Programming_ext = [ 
    '.db', 'sql', '.apk', '.bat', '.exe', '.app',
    '.jar',  '.html', '.htm', '.js', '.jsp', 
    '.php', '.css', '.aspx', '.asp', '.xhtml', 
    '.c', '.cpp', '.cs', '.java', '.lua', '.py', 
    '.sh', '.deb'

] 

Audio_ext = [
    '.mp3', '.wav', '.mid', '.m4a', '.aif'
]

Video_ext = [
    '.avi', '.mp4', '.mov', '.flv', '.mpg', '.m4v'
]

Image_ext = [
    '.bmp', '.gif', '.jpg', '.png', '.psd', 
    '.tif', 'tiff', '.dng', '.svg', '.ico',
    'jpeg'
]

Book_ext = [
    '.pdf'
]


# listing the base folder
files = listdir(base_folder)


def Organizing(Extension_list, destination_folder):
    for file in files:
        
        file = ("'" + file + "'")
        source = (base_folder + file)
        
        #print("File: " + file)
        #print("Source: " + source)

        for ext in Extension_list:
            if ext in file:
                system("mv " + source + " " + destination_folder)
                text = (file + " succesfully organised ")
                print(text)

Organizing(Document_ext, documents_folder)
Organizing(Programming_ext, programming_folder)
Organizing(Audio_ext, music_folder)
Organizing(Video_ext, videos_folder)
Organizing(Image_ext, images_folder)
Organizing(Book_ext, books_folder)

