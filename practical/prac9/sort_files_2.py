"""
Let the user categorise different extensions as the program encounters these, then move them all into those subdirectories.
"""
import os
import shutil


def main():
    """move files into subfolders where users want to put them on based on the extension."""
    extension_subfolders = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_extension = filename.split('.')[-1]  # split the file name and its extension by the '.'
        if file_extension not in extension_subfolders.keys():
            extension_category = input("What category would you like to sort {} files into? ".format(file_extension))
            extension_subfolders[
                file_extension] = extension_category  # add the extension_category as a value and file_extension as a key on extension_subfolder
            try:
                os.mkdir(extension_category)
            except FileExistsError:  # if the extension category dir have been made already
                pass
        shutil.move(filename, '{}/{}'.format(extension_subfolders[file_extension], filename))


main()
