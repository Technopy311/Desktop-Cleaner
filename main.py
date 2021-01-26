#!/usr/bin/python3

from os import listdir, system, path, getcwd
from pynotifier import Notification
#from shutil import move


#directory to be watched
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



print("Organizing")

#listing the base folder

files = listdir(base_folder)

for file in files:
    file = ("'" + file + "'")

    source = (base_folder + file)
    #print("File: " + file)
    #print("Source: " + source)

    
    for ext in Document_ext:
        if ext in file:
            system("mv " + source + " " + documents_folder)
            text = ("Moved " + file + " into Documents folder")
            Notification(
                title="Desktop succesfully organized",
                description=text,
                icon_path=None,
                duration=2,
                urgency=Notification.URGENCY_NORMAL,

            ).send()
            
    for ext in Programming_ext:
        if ext in file:
            system("mv " + source + " " + programming_folder)
            text = ("Moved " + file + " into programming folder")
            Notification(
                title="Desktop succesfully organized",
                description=text,
                icon_path=None,
                duration=2,
                urgency=Notification.URGENCY_NORMAL,

            ).send()
    
    for ext in Audio_ext:
        if ext in file:
            system("mv " + source + " " + music_folder)
            text = ("Moved " + file + " into Music folder")
            Notification(
                title="Desktop succesfully organized",
                description=text,
                icon_path=None,
                duration=2,
                urgency=Notification.URGENCY_NORMAL,

            ).send()

    for ext in Video_ext:
        if ext in file:
            system("mv " + source + " " + videos_folder)
            text = ("Moved " + file + " into Videos")
            Notification(
                title="Desktop succesfully organized",
                description=text,
                icon_path=None,
                duration=2,
                urgency=Notification.URGENCY_NORMAL,

            ).send()

    for ext in Image_ext:
        if ext in file:
            system("mv " + source + " " + images_folder)
            text = ("Moved " + file + " into Images folder")
            Notification(
                title="Desktop succesfully organized",
                description=text,
                icon_path=None,
                duration=2,
                urgency=Notification.URGENCY_NORMAL,

            ).send()

    for ext in Book_ext:
        if ext in file:
            system("mv " + source + " " + books_folder)
            text = ("Moved " + file + " into Books folder")
            Notification(
                title="Desktop succesfully organized",
                description=text,
                icon_path=None,
                duration=2,
                urgency=Notification.URGENCY_NORMAL,

            ).send()
    