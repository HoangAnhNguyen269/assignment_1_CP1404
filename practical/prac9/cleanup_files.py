"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files
        for filename in filenames:
            print(filename)
            print("Rename {} to {}".format(filename, get_fixed_filename(filename)))
            initial_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(initial_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    for i in range(len(filename)-1):
        if filename[i] == ' ':
            filename[i + 1].upper() #upper the first letter of word
        if filename[i].islower() and filename[i + 1].isupper():
            filename = filename[:i + 1] + '_' + filename[i + 1:] # add '_' between 2 words
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt") # add '_' between 2 words

    return new_name


main()
