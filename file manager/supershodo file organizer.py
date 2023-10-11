import os
import shutil

path = input("Enter Folder path:")
files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path, file)):
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        extension_folder = os.path.join(path, extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        shutil.move(os.path.join(path, file),
                    os.path.join(extension_folder, file))
