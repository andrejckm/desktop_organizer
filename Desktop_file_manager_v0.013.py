from os import scandir, rename, mkdir
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import sys
import time
import logging
import os
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# ! FILL IN BELOW IF DIRECTORY OF DESKTOP FOLDER IS DIFFERENT !

# ? folder to track e.g. Windows: "C:\\Users\\, os.getlogin(), \\Downloads"    ! os.getlogin() CALLS USER NAME FROM OS !
source_dir = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop"))
dest_dir_sfx = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\SFX"))
dest_dir_music = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\MUSIC"))
dest_dir_video = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\VIDEO"))
dest_dir_image = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\IMAGE"))
dest_dir_documents = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\DOCUMENTS"))
dest_dir_software = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\SOFTWARE"))
dest_dir_blender = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\BLENDER"))
dest_dir_script = "".join(("C:\\Users\\", os.getlogin(), "\\OneDrive\\Desktop\\SCRIPTS"))

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
# ? supported Software types
software_extensions = [".exe", ".rar", ".zip",
                       ".bat", ".msi"]
# ? supported Blender types
blender_extensions = [".blend", ".fbx", ".stl",
                       ".obj", ".ply", "x3d"]
# ? supported Script types
script_extensions = [".py", ".php", ".java",
                       ".html"]



def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    now = datetime.now()
    current_time = now.strftime("%Hh%Mm")
    
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}[{current_time}]){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# BLENDER #

pathblender = "C:\\Users\\andre\\OneDrive\\Desktop\\BLENDER"
# Check whether the specified path exists or not
isExist = os.path.exists(pathblender)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathblender)
  print("The new directory is created!")

# VIDEO #

pathvideo = "C:\\Users\\andre\\OneDrive\\Desktop\\VIDEO"
# Check whether the specified path exists or not
isExist = os.path.exists(pathvideo)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathvideo)
  print("The new directory is created!")

# IMAGE #

pathimage = "C:\\Users\\andre\\OneDrive\\Desktop\\IMAGE"
# Check whether the specified path exists or not
isExist = os.path.exists(pathimage)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathimage)
  print("The new directory is created!")

# SFX #

pathsfx = "C:\\Users\\andre\\OneDrive\\Desktop\\SFX"
# Check whether the specified path exists or not
isExist = os.path.exists(pathsfx)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathsfx)
  print("The new directory is created!")

# MUSIC #

pathmusic = "C:\\Users\\andre\\OneDrive\\Desktop\\MUSIC"
# Check whether the specified path exists or not
isExist = os.path.exists(pathmusic)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathmusic)
  print("The new directory is created!")

# SOFTWARE #

pathsoftware = "C:\\Users\\andre\\OneDrive\\Desktop\\SOFTWARE"
# Check whether the specified path exists or not
isExist = os.path.exists(pathsoftware)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathsoftware)
  print("The new directory is created!")

# DOCUMENTS #

pathdocument = "C:\\Users\\andre\\OneDrive\\Desktop\\DOCUMENTS"
# Check whether the specified path exists or not
isExist = os.path.exists(pathdocument)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathdocument)
  print("The new directory is created!")

# SCRIPTS #

pathscript = "C:\\Users\\andre\\OneDrive\\Desktop\\SCRIPTS"
# Check whether the specified path exists or not
isExist = os.path.exists(pathscript)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(pathscript)
  print("The new directory is created!")


class MoverHandler(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_software_files(entry, name)
                self.check_blender_files(entry, name)
                self.check_script_files(entry, name)


    def check_audio_files(self, entry, name):  # * Checks all Audio Files
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 3_000_000 or "SFX" in name:  # ? 3Megabytes
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # * Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_software_files(self, entry, name):  # * Checks all Software Files
        for software_extension in software_extensions:
            if name.endswith(software_extension) or name.endswith(software_extension.upper()):
                move_file(dest_dir_software, entry, name)
                logging.info(f"Moved software file: {name}")

    def check_blender_files(self, entry, name):  # * Checks all Software Files
        for blender_extension in blender_extensions:
            if name.endswith(blender_extension) or name.endswith(blender_extension.upper()):
                move_file(dest_dir_blender, entry, name)
                logging.info(f"Moved blender file: {name}")

    def check_script_files(self, entry, name):  # * Checks all Script Files
        for script_extension in script_extensions:
            if name.endswith(script_extension) or name.endswith(script_extension.upper()):
                move_file(dest_dir_script, entry, name)
                logging.info(f"Moved script file: {name}")


# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
