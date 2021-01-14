"""
sort these files  from FilesToSort into subdirectories for each extension.
"""
import os
import shutil
def main():
    """move files into subfolders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_extension=filename.split('.')[-1] #split the file name and its extension by the '.'
        try:
            os.mkdir(file_extension)
        except FileExistsError: #if the extension dir have been made already
            pass
        shutil.move(filename, '{}/{}'.format(file_extension,filename))

main()